{
    "name": "Tracking Serpost sale integration",
    "author": "Erick Navarro",
    "category": "Shipping Logistics",
    "license": "LGPL-3",
    "version": "0.1",
    "description": "Add Serpost tracking data to sale order",
    "depends": ["sale", "tracking_serpost"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/serpost_package_views.xml",
    ],
    "application": True,
}
