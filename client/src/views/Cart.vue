<template>
    <div>
        <h2 class="center-align">My Shopping Cart</h2>
        <CartDetail></CartDetail>
    </div>
</template>

<script>
    import CartDetail from "../components/CartDetail";

    export default {
        name: "Cart",
        components: {
            CartDetail: CartDetail
        }
    }
</script>

<style scoped>

</style>