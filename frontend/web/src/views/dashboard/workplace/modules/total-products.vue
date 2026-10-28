<template>
  <div class="fa-card h-53 p-5 pt-3.5">
    <div class="fa-card-header">
      <div class="title">
        <h4 class="text-2xl font-medium">42</h4>
        <p>打包产物</p>
      </div>
    </div>

    <FaBarChart
      :showAxisLabel="false"
      :showAxisLine="false"
      :showSplitLine="false"
      :data="[4, 6, 5, 8, 7, 12]"
      height="7rem"
      barWidth="18px"
    />
  </div>
</template>
