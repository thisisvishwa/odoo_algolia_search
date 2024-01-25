Developer Guide
===============

Welcome to the Developer Guide for the Advanced Algolia Search Integration for Odoo eCommerce v16. This guide will walk you through the technical aspects of integrating Algolia with your Odoo eCommerce platform.

Getting Started
---------------

Before you begin, ensure you have the following prerequisites:

- An active Algolia account with the necessary API keys (`ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, and `ALGOLIA_ADMIN_API_KEY`).
- Odoo v16 Open Source Edition installed and running.
- Basic knowledge of Python and Odoo development.

Installation
------------

To install the addon, follow the steps outlined in the `README.md` file under the `Installation` section.

Configuration
-------------

After installation, configure the addon by setting up the Algolia API keys and defining the index name (`ODOO_ALGOLIA_INDEX_NAME`). Refer to `doc/configuration_guide.rst` for detailed instructions.

Indexing Products
-----------------

The `AlgoliaIntegration` class in `models/algolia_integration.py` handles the synchronization of product data with Algolia. Use the `indexProductsToAlgolia` method to index your products. This method should be triggered whenever a product is created or updated.

Search Functionality
--------------------

The `AlgoliaSearchController` in `controllers/main.py` manages the search requests. The `searchWithAlgolia` method uses the Algolia API to fetch search results based on the user's query.

Autocomplete Feature
--------------------

The `algolia_autocomplete.js` file in `static/src/js/` contains the logic for the autocomplete feature. The `algoliaAutocomplete` function initializes the Algolia Autocomplete service.

Facet Filtering
---------------

Facet filtering is managed by the `handleFacetFilterChange` function in `algolia_autocomplete.js`. It updates the search results based on the selected filters.

Custom Searchable Fields
------------------------

To customize searchable fields, modify the `AlgoliaProduct` schema in `models/algolia_integration.py`. This schema defines the product data structure sent to Algolia.

Error Handling
--------------

Error handling for search and indexing operations is done through the `AlgoliaSearchError` and `AlgoliaIndexingError` messages. Ensure proper error handling in the integration to provide feedback to the user or system.

Testing
-------

Testing is crucial for ensuring the reliability of the addon. The `tests/test_algolia_integration.py` file contains unit and integration tests. Follow the naming conventions for test functions, such as `test_algolia_integration` and `test_algolia_search`.

UI/UX Integration
-----------------

The search interface is defined in `views/algolia_search_templates.xml`. Customize the UI/UX by editing this file and the corresponding CSS in `static/src/css/algolia_styles.css`.

Security
--------

Security rules are defined in `security/ir.model.access.csv` and `security/algolia_security.xml`. Ensure that access controls are correctly set up for different user levels.

Conclusion
----------

This guide provides an overview of the development process for the Advanced Algolia Search Integration for Odoo eCommerce v16. For more detailed information, refer to the specific guides in the `doc/` directory. Happy coding!