odoo.define('algolia_integration.algolia_autocomplete', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');

    publicWidget.registry.AlgoliaAutocomplete = publicWidget.Widget.extend({
        selector: '#algolia-search-input',
        events: {
            'keyup': '_onKeyup',
            'focus': '_onFocus',
        },
        start: function() {
            this._super.apply(this, arguments);
            this._initAlgoliaClient();
        },
        _initAlgoliaClient: function() {
            this.algoliaClient = algoliasearch(ALGOLIA_APP_ID, ALGOLIA_SEARCH_API_KEY);
            this.algoliaIndex = this.algoliaClient.initIndex(ODOO_ALGOLIA_INDEX_NAME);
        },
        _onKeyup: function(ev) {
            var self = this;
            var query = $(ev.currentTarget).val();
            if (query.length > 0) {
                this.algoliaIndex.search(query, {
                    hitsPerPage: 5,
                    highlightPreTag: '<em>',
                    highlightPostTag: '</em>'
                }).then(function(responses) {
                    self._renderSuggestions(responses.hits);
                }).catch(function(err) {
                    console.error(err);
                });
            } else {
                this._clearSuggestions();
            }
        },
        _onFocus: function() {
            this.$('#algolia-autocomplete-dropdown').show();
        },
        _renderSuggestions: function(suggestions) {
            var $dropdown = this.$('#algolia-autocomplete-dropdown');
            var html = '';
            suggestions.forEach(function(suggestion) {
                html += '<div class="algolia-autocomplete-item">';
                html += '<span>' + suggestion._highlightResult.name.value + '</span>';
                html += '</div>';
            });
            $dropdown.html(html).show();
        },
        _clearSuggestions: function() {
            this.$('#algolia-autocomplete-dropdown').empty().hide();
        },
    });

    return {
        AlgoliaAutocomplete: publicWidget.registry.AlgoliaAutocomplete,
    };
});