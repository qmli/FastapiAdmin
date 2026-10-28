<template>
  <div class="fa-card p-5 h-138 overflow-hidden">
    <div class="fa-card-header">
      <div class="title">
        <h4>构建待办</h4>
        <p>
          待处理
          <span class="text-danger">{{ pendingCount }}</span>
        </p>
      </div>
    </div>

    <ElScrollbar class="h-[calc(100%-40px)]" view-style="padding-right: 16px">
      <div
        class="flex items-center justify-between h-17.5 border-b border-g-300 text-sm last:border-b-0"
        v-for="item in list"
        :key="item.target"
      >
        <div>
          <p class="text-sm">
            <span class="text-g-800 font-medium">{{ item.owner }}</span>
            <span class="mx-2 text-g-600">{{ item.action }}</span>
            <span class="text-theme">{{ item.target }}</span>
          </p>
          <p class="text-g-500 mt-1">{{ item.time }}</p>
        </div>
        <ElCheckbox v-model="item.done" />
      </div>
    </ElScrollbar>
  </div>
</template>

<script setup lang="ts">
interface BuildTodo {
  owner: string;
  time: string;
  done: boolean;
  action: string;
  target: string;
}

const list = reactive<BuildTodo[]>([
  {
    owner: "编译",
    time: "上午 09:18",
    done: false,
    action: "重试",
    target: "#BSW-1048",
  },
  {
    owner: "打包",
    time: "上午 10:05",
    done: false,
    action: "签名",
    target: "#PKG-241",
  },
  {
    owner: "构建",
    time: "上午 11:20",
    done: false,
    action: "确认",
    target: "#BLD-780",
  },
  {
    owner: "制品库",
    time: "上午 08:40",
    done: true,
    action: "发布",
    target: "bsw-core 2.4.1",
  },
  {
    owner: "编译",
    time: "上午 08:10",
    done: true,
    action: "查看",
    target: "#CC-019",
  },
]);

const pendingCount = computed(() => list.filter((item) => !item.done).length);
</script>
