# -*- coding: utf-8 -*-
{
    'name': "Gestion de biblioteca",
    'summary': """Gestión del catálogo de la biblioteca y los prestamos de libros """,
    'author': "Miguel Vidal Tordillo",
    'license': "AGPL-3",
    'website': "https://github.com/mvidalt",
    'version': '1.0',
    'depends': ['base'],
    'application': True,
    'category': "Services/Library",

    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ]
}
