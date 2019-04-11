<template>
    <div class="row">
        <div class="col l12">
            <table class="highlight responsive-table">
                <thead>
                <tr>
                    <th>Image</th>
                    <th>Product</th>
                    <th>Description</th>
                    <th>Variant</th>
                    <th>Price</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item, index) in getCartItems" :key="index">
                    <td><img :src="item.image" :alt="item.product_name" height="100px"></td>
                    <td>{{ item.product_name }}</td>
                    <td>{{ item.product_description }}</td>
                    <td>{{ item.variant_name }}</td>
                    <td>${{ item.price }}</td>
                </tr>
                <tr v-if="getSum > 0">
                    <td></td>
                    <td></td>
                    <td></td>
                    <td>Total</td>
                    <td>${{ getSum }}</td>
                </tr>
                </tbody>
            </table>
        </div>
        <div v-if="getSum > 0" id="cart-action" class="col l12 right-align">
            <a class="btn">Checkout</a>
            <a @click="clearCart" class="btn red">Clear Cart</a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CartDetail",
        computed: {
            getCartItems() {
                return this.$store.getters.cartItems;
            },
            getSum() {
                return this.$store.getters.sumCartItems;
            }
        },
        methods:{
            clearCart(){
                this.$store.commit('cleanCart')
            }
        }
    }
</script>

<style scoped>
    #cart-action {
        margin-top: 2em;
    }

    #cart-action .btn {
        margin-left: 5px;
    }
</style>