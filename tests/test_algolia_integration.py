from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestAlgoliaIntegration(TransactionCase):

    def setUp(self):
        super(TestAlgoliaIntegration, self).setUp()
        self.AlgoliaIntegration = self.env['algolia.integration']
        # Setup test data if needed

    def test_algolia_integration_access_rights(self):
        # Test that users cannot access Algolia integration without proper rights
        with self.assertRaises(AccessError):
            self.AlgoliaIntegration.sudo(self.env.ref('base.user_demo')).search([])

    def test_algolia_integration(self):
        # Test the basic functionality of Algolia integration
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Integration',
            'algolia_app_id': 'test_app_id',
            'algolia_search_api_key': 'test_search_key',
            'algolia_admin_api_key': 'test_admin_key',
            'odoo_algolia_index_name': 'test_index'
        })
        self.assertTrue(algolia_integration, "Algolia Integration record should be created")

    def test_index_products_to_algolia(self):
        # Test indexing of products to Algolia
        product_template = self.env['product.template'].create({
            'name': 'Test Product',
            'list_price': 10.0,
            'standard_price': 5.0
        })
        self.assertTrue(product_template, "Product Template should be created")
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Integration',
            'algolia_app_id': 'test_app_id',
            'algolia_search_api_key': 'test_search_key',
            'algolia_admin_api_key': 'test_admin_key',
            'odoo_algolia_index_name': 'test_index'
        })
        algolia_integration.indexProductsToAlgolia([product_template.id])
        # Add assertions to check if the product was indexed correctly

    def test_algolia_search(self):
        # Test search functionality with Algolia
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Integration',
            'algolia_app_id': 'test_app_id',
            'algolia_search_api_key': 'test_search_key',
            'algolia_admin_api_key': 'test_admin_key',
            'odoo_algolia_index_name': 'test_index'
        })
        search_results = algolia_integration.searchWithAlgolia('Test Product')
        # Add assertions to check if the search results are as expected

    def test_update_algolia_index(self):
        # Test updating the Algolia index when products change
        product_template = self.env['product.template'].create({
            'name': 'Test Product',
            'list_price': 10.0,
            'standard_price': 5.0
        })
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Integration',
            'algolia_app_id': 'test_app_id',
            'algolia_search_api_key': 'test_search_key',
            'algolia_admin_api_key': 'test_admin_key',
            'odoo_algolia_index_name': 'test_index'
        })
        product_template.write({'name': 'Updated Test Product'})
        algolia_integration.updateAlgoliaIndex([product_template.id])
        # Add assertions to check if the Algolia index is updated correctly

    def tearDown(self):
        # Clean up after tests if needed
        pass