<template>
  <div class="fa-card h-82 p-5 mb-5 max-sm:mb-4">
    <div class="fa-card-header">
      <div class="title">
        <h4>功能占比</h4>
        <p>通信、诊断与模式管理</p>
      </div>
    </div>

    <FaRingChart
      :data="[
        { value: 186, name: '通信' },
        { value: 96, name: '诊断' },
        { value: 130, name: '模式管理' },
      ]"
      :color="['#4C87F3', '#93F1B4', '#8BD8FC']"
      :radius="['46%', '60%']"
    />
  </div>
</template>
