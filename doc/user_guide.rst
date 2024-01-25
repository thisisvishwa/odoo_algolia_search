User Guide
==========

Welcome to the Advanced Algolia Search Integration for Odoo eCommerce v16 user guide. This document will guide you through the process of using the Algolia search integration on your Odoo v16 eCommerce website.

Installation
------------

Before you can use the Algolia search integration, you need to install the addon. Please refer to the `Installation` section in the README.md file for detailed instructions on how to install the addon on your Odoo instance.

Configuration
-------------

Once the addon is installed, you need to configure it to connect to your Algolia account.

1. Navigate to the Odoo backend and go to `Website` -> `Configuration` -> `Settings`.
2. Look for the `Algolia Search` section.
3. Enter your `ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, and `ALGOLIA_ADMIN_API_KEY`.
4. Set the `ODOO_ALGOLIA_INDEX_NAME` to the name of the index you want to use in Algolia.
5. Save the settings.

For more detailed instructions, please refer to the `configuration_guide.rst` in the `doc` directory.

Using Algolia Search on Your Website
------------------------------------

After configuring the addon, the Algolia search bar will be available on your Odoo website.

### Performing a Search

1. Go to your website's homepage.
2. You will find the Algolia search bar prominently displayed.
3. Start typing your query into the search bar.
4. As you type, autocomplete suggestions will appear in a dropdown below the search bar.
5. Select a suggestion or complete your query and press `Enter` to see the full search results.

### Using Facet Filters

1. On the search results page, you will see a list of facet filters on the side.
2. Click on the filters to narrow down your search by category, brand, price, size, color, etc.
3. The product list will update dynamically as you apply filters.

### Viewing Product Details

1. In the search results, each product will have an image, title, description, and price displayed.
2. Hover over a product to see more details or click on it to go to the product page.

Search Analytics
----------------

The Algolia search integration provides valuable insights into user search behavior.

1. To view search analytics, navigate to `Website` -> `Configuration` -> `Algolia Dashboard`.
2. Here you can see popular keywords, abandoned searches, and conversion rates from search.

Troubleshooting
---------------

If you encounter any issues while using the Algolia search integration, please refer to the `doc/developer_guide.rst` for troubleshooting tips or contact your system administrator.

Conclusion
----------

The Advanced Algolia Search Integration for Odoo eCommerce v16 is designed to enhance your customers' search experience. By following this guide, you should be able to effectively use the search functionalities on your website. For further assistance, please consult the additional documentation provided with this addon.