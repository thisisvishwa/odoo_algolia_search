# Advanced Algolia Search Integration for Odoo eCommerce v16

## Author
Bard (AI Assistant)

## Date
2024-01-25

## Version
1.0

## Introduction
This README provides an overview and guidance for installing and configuring the Advanced Algolia Search Integration for Odoo eCommerce v16. This addon enhances the default search capabilities of Odoo's eCommerce platform by integrating with Algolia's powerful search engine.

## Installation

To install this addon, follow these steps:

1. Ensure you have Odoo v16 Open Source edition installed.
2. Download or clone the addon from the repository.
3. Place the addon folder in your Odoo addons directory.
4. Restart your Odoo server.
5. Activate the developer mode in Odoo.
6. Go to Apps -> Update Apps List.
7. Search for 'Advanced Algolia Search Integration' and click Install.

## Configuration

After installation, you need to configure the addon:

1. Navigate to the Odoo backend and go to Website -> Configuration -> Settings.
2. Locate the Algolia Search Integration section.
3. Enter your `ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, and `ALGOLIA_ADMIN_API_KEY`.
4. Set the `ODOO_ALGOLIA_INDEX_NAME` to the name of your Algolia index.
5. Configure additional searchable fields and facet filters as needed.

For detailed configuration instructions, please refer to the `doc/configuration_guide.rst`.

## Usage

Once configured, the Algolia search bar will be available on your Odoo eCommerce website. Customers can start typing in the search bar to see instant suggestions, facet filters, and rich product previews.

For more information on how to use the addon, please refer to the `doc/user_guide.rst`.

## Documentation

Comprehensive documentation is provided to help you understand and make the most of this addon:

- `doc/index.rst`: Entry point for the documentation.
- `doc/changelog.rst`: Information on the changes and version history.
- `doc/configuration_guide.rst`: Detailed configuration instructions.
- `doc/developer_guide.rst`: Guidelines for developers who wish to customize or extend the addon.
- `doc/user_guide.rst`: Instructions for end-users on how to use the search features.

## Support

If you encounter any issues or require support, please refer to the `doc/developer_guide.rst` for troubleshooting tips or contact the addon developers.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.