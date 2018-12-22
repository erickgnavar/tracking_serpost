{
    "name": "Tracking Serpost purchase integration",
    "author": "Erick Navarro",
    "category": "package",
    "license": "LGPL-3",
    "version": "0.1",
    "description": "Add Serpost tracking data to purchase order",
    "depends": ["purchase", "tracking_serpost"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_views.xml",
        "views/serpost_package_views.xml",
    ],
    "application": True,
}
