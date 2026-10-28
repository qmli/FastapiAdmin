<template>
  <div class="fa-card flex flex-col p-5 h-138 overflow-hidden">
    <div class="mb-3">
      <div class="title">
        <h4 class="text-lg font-medium text-g-900">最近任务</h4>
        <p class="mt-1 text-sm text-g-600">编译、打包与构建流水线</p>
      </div>
      <ElRadioGroup v-model="kind" size="small" class="mt-3">
        <ElRadioButton value="全部" label="全部" />
        <ElRadioButton value="编译" label="编译" />
        <ElRadioButton value="打包" label="打包" />
        <ElRadioButton value="构建" label="构建" />
      </ElRadioGroup>
    </div>
    <FaTable
      class="w-full"
      :data="filteredJobs"
      :border="false"
      :stripe="false"
      :header-cell-style="{ background: 'transparent' }"
    >
      <template #default>
        <ElTableColumn label="任务" min-width="140">
          <template #default="scope">
            <div class="font-medium">{{ scope.row.name }}</div>
            <div class="text-xs text-slate-500">
              {{ scope.row.target }} · {{ scope.row.trigger }} · {{ scope.row.duration }}
            </div>
          </template>
        </ElTableColumn>
        <ElTableColumn label="类型" prop="type" width="72" />
        <ElTableColumn label="状态" width="88">
          <template #default="scope">
            <ElTag :type="statusType(scope.row.status)" size="small" effect="light">
              {{ scope.row.status }}
            </ElTag>
          </template>
        </ElTableColumn>
      </template>
    </FaTable>
  </div>
</template>

<script setup lang="ts">
import FaTable from "@/components/tables/fa-table/index.vue";

type JobKind = "编译" | "打包" | "构建";
type JobStatus = "成功" | "失败" | "进行中" | "排队";

interface BuildJob {
  name: string;
  target: string;
  type: JobKind;
  status: JobStatus;
  duration: string;
  trigger: string;
}

const kind = ref<"全部" | JobKind>("全部");

const jobs: BuildJob[] = [
  {
    name: "基础软件 BSW",
    target: "linux-aarch64",
    type: "编译",
    status: "成功",
    duration: "6分12秒",
    trigger: "定时",
  },
  {
    name: "工具链安装包",
    target: "x86_64",
    type: "打包",
    status: "成功",
    duration: "3分40秒",
    trigger: "手动",
  },
  {
    name: "网关配置",
    target: "qnx",
    type: "构建",
    status: "失败",
    duration: "8分05秒",
    trigger: "提交",
  },
  {
    name: "诊断协议栈",
    target: "linux-arm",
    type: "编译",
    status: "进行中",
    duration: "2分18秒",
    trigger: "提交",
  },
  {
    name: "运行时组件",
    target: "x86_64",
    type: "打包",
    status: "排队",
    duration: "—",
    trigger: "手动",
  },
  {
    name: "通信栈",
    target: "linux-aarch64",
    type: "构建",
    status: "成功",
    duration: "11分26秒",
    trigger: "定时",
  },
];

const filteredJobs = computed(() =>
  kind.value === "全部" ? jobs : jobs.filter((job) => job.type === kind.value)
);

const statusType = (status: JobStatus) => {
  if (status === "成功") return "success";
  if (status === "失败") return "danger";
  if (status === "进行中") return "warning";
  return "info";
};
</script>

<style lang="scss" scoped>
.fa-card {
  :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
    color: var(--el-color-primary) !important;
    background: transparent !important;
  }
}
</style>
