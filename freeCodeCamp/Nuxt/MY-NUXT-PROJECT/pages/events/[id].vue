
<script setup>
const nuxtApp = useNuxtApp();
const route = useRoute();

console.log(nuxt);
console.log(route.params.id);
</script>

<template>
    <div>
        events id: {{ $route.params.id }}
    </div>
</template>
