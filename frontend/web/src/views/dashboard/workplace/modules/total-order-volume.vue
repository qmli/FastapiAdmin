<template>
  <div class="fa-card h-53 p-5 pt-3.5">
    <div class="fa-card-header">
      <div class="title">
        <h4 class="text-2xl font-medium">412</h4>
        <p>本月构建</p>
      </div>
    </div>

    <FaRingChart
      :data="[
        { value: 368, name: '成功' },
        { value: 28, name: '失败' },
        { value: 16, name: '排队' },
      ]"
      :color="['#4C87F3', '#93F1B4', '#8BD8FC']"
      :radius="['56%', '76%']"
      height="7rem"
      :showLabel="false"
      :borderRadius="0"
    />
  </div>
</template>
