#!/usr/bin/env python
"""
Utilitaire de gestion Django pour les tâches administratives.
"""

import os
import sys

def main():
    """Exécute les tâches administratives."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trustia_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Assurez-vous que Django est installé "
            "et disponible dans votre environnement."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
