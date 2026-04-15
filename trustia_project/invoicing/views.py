from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product, Invoice, InvoiceItem
from .forms import ProductForm, InvoiceForm, InvoiceItemForm


class ProductListView(ListView):
    model = Product
    template_name = 'invoicing/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'invoicing/product_form.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produit créé avec succès !')
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'invoicing/product_form.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Produit modifié avec succès !')
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'invoicing/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Produit supprimé avec succès !')
        return super().delete(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'invoicing/product_detail.html'
    context_object_name = 'product'


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoicing/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10
    
    def get_queryset(self):
        return Invoice.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for invoice in context['invoices']:
            invoice.total_amount = invoice.get_total_amount()
        return context


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoicing/invoice_form.html'
    success_url = reverse_lazy('invoice_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Facture créée avec succès !')
        self.object = form.save()
        return redirect('invoice_add_items', pk=self.object.pk)


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoicing/invoice_detail.html'
    context_object_name = 'invoice'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        context['total_amount'] = self.object.get_total_amount()
        context['total_quantity'] = self.object.get_total_quantity()
        return context


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoicing/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Facture supprimée avec succès !')
        return super().delete(request, *args, **kwargs)


def invoice_add_items(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    products = Product.objects.all()
    
    if request.method == 'POST':
        for product_id in request.POST.getlist('product_ids'):
            quantity = request.POST.get(f'quantity_{product_id}')
            if quantity and int(quantity) > 0:
                product = get_object_or_404(Product, pk=product_id)
                InvoiceItem.objects.update_or_create(
                    invoice=invoice,
                    product=product,
                    defaults={
                        'quantity': int(quantity),
                        'unit_price': product.price
                    }
                )
        messages.success(request, 'Produits ajoutés à la facture !')
        return redirect('invoice_detail', pk=pk)
    
    invoiced_products = InvoiceItem.objects.filter(invoice=invoice).values_list('product_id', 'quantity')
    invoiced_dict = {item[0]: item[1] for item in invoiced_products}
    
    context = {
        'invoice': invoice,
        'products': products,
        'invoiced_dict': invoiced_dict,
    }
    return render(request, 'invoicing/invoice_add_items.html', context)


def invoice_remove_item(request, invoice_id, item_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    item = get_object_or_404(InvoiceItem, pk=item_id, invoice=invoice)
    item.delete()
    messages.success(request, 'Produit supprimé de la facture !')
    return redirect('invoice_detail', pk=invoice_id)
