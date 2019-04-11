<template>
    <div>
        <div class="row">
            <div class="col s12 center-align">
                <img id="logo-store" :src=store.logo :alt=store.name>
            </div>
            <div class="col s12">
                <blockquote>
                    <h4>{{ store.name | capitalize }}</h4> - {{ store.slogan | capitalize }}
                </blockquote>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m6 l4" v-for="product in products" :key="product.slug">
                <div class="card">
                    <div class="card-image">
                        <img :src="get_image(product)" :alt=product.name>
                        <a v-if="get_stock(product) > 0" @click="add_to_cart()"
                           class="btn-floating halfway-fab waves-effect waves-light red" title="Add to Cart">
                            <i class="material-icons">add_shopping_cart</i>
                        </a>
                    </div>
                    <div class="card-content">
                        <span class="card-title red-text text-accent-3">{{ product.name }}</span>
                        <p>{{ product.description }}</p>
                        <p v-if="get_price(product) > 0"><strong>Precio: ${{ get_price(product)}}</strong></p>
                        <p v-if="get_stock(product) > 0"><strong>Unidades disponibles: {{ get_stock(product)}}</strong>
                        </p>
                    </div>
                    <div class="card-action">
                        <ProductVariants @hoverVariant="updateImage" :slug=product.slug></ProductVariants>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import ProductVariants from "./ProductVariants";

    export default {
        name: "StoreDetail",
        data() {
            return {
                store: Object,
                products: [],
                loading: true,
                errored: false,
                image: '',
                selected: null,
                selected_variant: null,
            }
        },
        components: {
            ProductVariants: ProductVariants
        },
        methods: {
            updateImage(variant, product) {
                this.selected_variant = variant;
                this.selected = product;
            },
            get_image(product) {
                if (this.selected != null && this.selected.url === product.url) {
                    return this.selected_variant.image;
                }
                return product.image
            },
            get_price(product) {
                if (this.selected != null && this.selected.url === product.url) {
                    return this.selected_variant.price;
                }
                return 0
            },
            get_stock(product) {
                if (this.selected != null && this.selected.url === product.url) {
                    return this.selected_variant.stock;
                }
                return 0
            },
            add_to_cart() {
                let item = {};
                item.product_name = this.selected.name;
                item.product_description = this.selected.description;
                item.variant_name = this.selected_variant.name;
                item.image = this.selected_variant.image;
                item.price = this.selected_variant.price;
                this.$store.commit('addProduct', item);
            }
        },
        props: {
            slug: String
        },
        filters: {
            capitalize: function (value) {
                if (!value) return '';
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase();
            }
        },
        mounted: function () {
            axios.get('https://peiky-python.herokuapp.com/api/stores/?format=json&slug=' + this.slug)
                .then(response => {
                    this.store = response.data.results.pop();
                    this.products = this.store.product_set;
                })
                .catch(error => {
                    alert(error);
                    this.errored = true
                })
                .finally(() => this.loading = false)
        }
    }
</script>

<style scoped>
#logo-store {
    width: 250px;
    padding: 10px;
}
</style>