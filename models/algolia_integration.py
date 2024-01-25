from odoo import models, fields, api
from algoliasearch.search_client import SearchClient

class AlgoliaIntegration(models.Model):
    _name = 'algolia.integration'
    _description = 'Algolia Integration for Odoo eCommerce'

    ALGOLIA_APP_ID = fields.Char(string='Algolia Application ID', required=True)
    ALGOLIA_SEARCH_API_KEY = fields.Char(string='Algolia Search-Only API Key', required=True)
    ALGOLIA_ADMIN_API_KEY = fields.Char(string='Algolia Admin API Key', required=True)
    ODOO_ALGOLIA_INDEX_NAME = fields.Char(string='Algolia Index Name', required=True)

    @api.model
    def _get_algolia_client(self):
        return SearchClient.create(self.ALGOLIA_APP_ID, self.ALGOLIA_ADMIN_API_KEY)

    @api.model
    def _prepare_product_data_for_algolia(self, product):
        algolia_product = {
            'objectID': product.id,
            'name': product.name,
            'description': product.description_sale,
            'price': product.list_price,
            'image': product.image_1920,
            # Add any other product fields you want to index
        }
        return algolia_product

    @api.model
    def indexProductsToAlgolia(self):
        client = self._get_algolia_client()
        index = client.init_index(self.ODOO_ALGOLIA_INDEX_NAME)
        products = self.env['product.template'].search([])
        algolia_products = [self._prepare_product_data_for_algolia(product) for product in products]
        index.save_objects(algolia_products)

    @api.model
    def updateAlgoliaIndex(self, product):
        client = self._get_algolia_client()
        index = client.init_index(self.ODOO_ALGOLIA_INDEX_NAME)
        algolia_product = self._prepare_product_data_for_algolia(product)
        index.partial_update_object(algolia_product)

    @api.model
    def searchWithAlgolia(self, query, filters=None):
        client = self._get_algolia_client()
        index = client.init_index(self.ODOO_ALGOLIA_INDEX_NAME)
        search_params = {
            'hitsPerPage': 10,
            'filters': filters,
        }
        return index.search(query, search_params)