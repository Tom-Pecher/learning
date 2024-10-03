
<template>
  <div>
    <NuxtLayout>
      <Header />
        <ul>
          <li>
            <NuxtLink to="/">Home</NuxtLink>
            <NuxtLink to="/events">Events</NuxtLink>
          </li>
        </ul>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
