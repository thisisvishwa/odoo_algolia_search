Configuration Guide
===================

This guide provides instructions on how to configure the Advanced Algolia Search Integration for Odoo eCommerce v16.

Prerequisites
-------------

Before you begin the configuration process, ensure that you have:

- Installed the Advanced Algolia Search Integration addon.
- A valid Algolia account with access to the necessary APIs.

Configuration Steps
-------------------

1. Algolia Account Setup
   - Log in to your Algolia account.
   - Navigate to the 'API Keys' section and retrieve your `ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, and `ALGOLIA_ADMIN_API_KEY`.

2. Odoo Configuration
   - Go to Odoo and log in as an administrator.
   - Navigate to the Apps module and install the Advanced Algolia Search Integration addon if you haven't already.

3. Algolia Credentials in Odoo
   - In Odoo, go to `Settings` > `Algolia Integration`.
   - Enter your Algolia credentials (`ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, and `ALGOLIA_ADMIN_API_KEY`) in the respective fields.
   - Save the changes.

4. Index Configuration
   - Set the `ODOO_ALGOLIA_INDEX_NAME` to the name of the index you wish to use in Algolia.
   - Use the `indexProductsToAlgolia` method to index your existing product database to Algolia.

5. Search Bar Customization
   - Access the `algolia_backend_view_form` to customize the search bar appearance.
   - Define the placeholder text, styling, and any other visual elements as per your website's design.

6. Facet Filters Setup
   - In the Algolia backend view, specify the facet filters you want to use by creating `AlgoliaFacetFilter` records.
   - Configure the facet attributes such as category, brand, price, etc., that you want to be filterable in your search.

7. Searchable Fields
   - Define which product attributes should be searchable by configuring the `AlgoliaProduct` schema.
   - You can include attributes like name, description, tags, etc.

8. Autocomplete and Instant Search
   - Enable the `algolia_autocomplete.js` script in your website's frontend to activate the autocomplete feature.
   - Customize the `#algolia-autocomplete-dropdown` to match your site's design.

9. Testing
   - Perform a test search to ensure that the integration is working correctly.
   - Check the instant search results and facet filters for expected behavior.

10. Analytics and Reporting
    - Use the `searchWithAlgolia` function to track search analytics.
    - Review the search reports in your Algolia dashboard to gain insights and optimize your search setup.

For detailed information on each step, refer to the `developer_guide.rst` and `user_guide.rst` documentation files.

Troubleshooting
---------------

If you encounter any issues during the configuration process, please refer to the `README.md` file for troubleshooting tips or contact support for assistance.