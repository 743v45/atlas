=== tdesign skyline progress issue:
3149
🚀 Skyline：组件适配进度
> 累计 35 个组件，占全体组件的 61% (35/57)。
>  建议使用 Android终端，微信 8.0.49 版本体验完整的功能，其他终端或微信版本会存在非预期表现。

- [x] Button  按钮
- [x] Divider 分割线
- [x] Fab 悬浮按钮
- [x] Icon 图标
- [x] Layout 布局
- [x] Link 链接
- [x] BackTop 返回顶部
- [x] Drawer 抽屉
- [x] Navbar 导航栏
- [x] Steps 步骤条
- [x] TabBar 标签栏
- [x] CheckBox多选框组
- [x] Input 输入框
- [x] Radio 单选框
- [x] Search 搜索框
- [x] Stepper 步进器
- [x] Switch 开关
- [x] Textarea 多行文本框
- [x] Avatar 头像
- [x] Badge 徽标
- [x] Cell 单元格
- [x] CountDown 倒计时
- [x] Empty 空状态
- [x] Footer 页脚
- [x] Image 图片
- [x] ImageViewer 图片预览
- [x] Progress 进度条
- [x] Result 结果
- [x] Skeleton 骨架屏
- [x] Tag 标签
- [x] Loading 加载
- [x] Overlay 遮罩层
- [x] Popup 弹出层
- [x] Toast 轻提示
- [ ] SideBar 侧边栏
- [ ] Tabs 选项卡
- [ ] Calendar 日历
- [ ] Cascader 级联选择器
- [ ] ColorPicker 颜色选择器
- [ ] DateTimePicker 时间选择器
- [ ] Picker 选择器
- [ ] Rate 评分
- [ ] Slider 滑动选择器
- [ ] TreeSelect 树形选择
- [ ] Upload 上传
- [ ] Collapse 折叠面板
- [ ] Grid 宫格
- [ ] Sticky 吸顶
- [ ] Swiper 轮播图
- [ ] ActionSheet 动作面板
- [ ] Dialog 对话框
- [ ] DropdownMenu 下拉菜单
- [ ] Guide 引导
- [ ] Message 消息通知
- [ ] NoticeBar 公告栏
- [ ] PullDo
=== wot-design-uni skyline issue (closed 2026-09):
issue #317
希望组件能够适配skyline
有计划支持



---原始邮件---
发件人: ***@***.***&gt;
发送时间: 2024年5月16日(周四) 凌晨0:25
收件人: ***@***.***&gt;;
抄送: ***@***.***&gt;;
主题: [Moonofweisheng/wot-design-uni] 希望组件能够适配skyline (Issue #317)




 
这个功能解决了什么问题？
 
适配微信新渲染引擎，优化渲染速度
 
你期望的 API 是什么样子的？
 
.
 
—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you are subscribed to this thread.Message ID: ***@***.***&gt;
工作量有点大，比如 
1. Skyline 遵循标准规范，要求伪元素使用 ::before 而不是 :before
2. Skyline 不支持 gap 属性
