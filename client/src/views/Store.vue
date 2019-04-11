<template>
    <div>
        <StoreDetail :slug="$route.params.slug" ></StoreDetail>
    </div>
</template>

<script>
    import StoreDetail from "@/components/StoreDetail";

    export default {
        name: "Store",
        components: {
            StoreDetail: StoreDetail
        },
        props: {
            store: Object,
        }
    }
</script>

<style scoped>

</style>