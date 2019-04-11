<template>
    <div>
        <a :class="isActive(variant)" @mouseover="updateSelected(variant)" v-for="variant in variants" :key="variant.id">
            {{ variant.name }}
        </a>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "ProductVariants",
        data() {
            return {
                product: null,
                variants: null,
                loading: true,
                errored: false,
                selected: null
            }
        },
        props: {
            slug: String
        },
        methods:{
            updateSelected(variant) {
                this.selected = variant;
                this.$emit('hoverVariant', variant, this.product)
            },
            isActive(variant) {
                if (variant === this.selected) {
                    return "btn-flat orange white-text";
                } else {
                    return "btn-flat";
                }
            }
        },
        mounted: function () {
            axios.get('https://peiky-python.herokuapp.com/api/products/?format=json&slug=' + this.slug)
                .then(response => {
                    this.product = response.data.results.pop();
                    this.variants = this.product.variant_set;
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

</style>