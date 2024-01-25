from odoo import http
from odoo.http import request
import json

class AlgoliaSearchController(http.Controller):

    @http.route('/shop/algolia_search', type='json', auth='public', website=True)
    def algolia_search(self, **post):
        search_query = post.get('search_query', '')
        filters = post.get('filters', '')
        algolia_client = request.env['algolia.integration']._get_algolia_client()
        index = algolia_client.init_index(ODOO_ALGOLIA_INDEX_NAME)

        try:
            # Perform the search on Algolia
            search_result = index.search(search_query, {
                'facetFilters': filters
            })
            return {
                'success': True,
                'results': search_result['hits'],
                'facets': search_result.get('facets', {})
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    @http.route('/shop/algolia_facet_filter', type='json', auth='public', website=True)
    def algolia_facet_filter(self, **post):
        facet_name = post.get('facet_name', '')
        facet_value = post.get('facet_value', '')
        algolia_client = request.env['algolia.integration']._get_algolia_client()
        index = algolia_client.init_index(ODOO_ALGOLIA_INDEX_NAME)

        try:
            # Perform the search with facet filters on Algolia
            search_result = index.search('', {
                'facetFilters': [[f'{facet_name}:{facet_value}']]
            })
            return {
                'success': True,
                'results': search_result['hits'],
                'facets': search_result.get('facets', {})
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }