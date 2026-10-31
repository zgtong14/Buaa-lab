# 自动同步 Google Scholar 论文

`Sync Google Scholar publications` 每两周一次，在隔周一北京时间约 07:23 检查 `_data/socials.yml` 中的 `scholar_userid`（当前为童志国的主页）。以 2026-11-02 为首个检查周，之后为 11 月 16 日、11 月 30 日等。GitHub 定时任务可能延迟；新论文需先出现在该 Scholar 主页中。

工作流每周触发一次轻量日期判断，只在隔周执行实际抓取；手动运行不受日期限制。

首次使用只需将脚本和工作流提交、推送到默认分支。在 GitHub **Actions → Sync Google Scholar publications → Run workflow** 可以立即运行，并查看新增数量或失败日志。

## 更新范围

- 新论文追加到 `_bibliography/papers.bib`，按 Scholar ID、DOI 或规范化标题去重。
- 保留所有已有条目及手工设置的 PDF、精选标记和作者信息，不自动删除或改写旧论文。
- 新条目进入“全部论文”，默认 `selected = {false}`；如需在首页精选展示，手动改为 `true`。
- 常见刊会自动匹配简称。不自动下载 PDF；需要公开的 PDF 可以后续手工添加。
- Scholar 只有整段来源信息、未提供独立刊会字段时，按 `misc` 保存并原样展示来源，不猜测刊会名称。标题中丢失的数字公式片段也会参与保守去重。
- 为避免重复，同名的会议和期刊版本会保守地视为同一条，需手工补充确有必要独立展示的版本。

有新增时，工作流提交论文列表，然后显式启动 `Deploy site`。这是因为使用 `GITHUB_TOKEN` 推送的提交不会自动触发另一个 push 工作流，参见 [GitHub 官方说明](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)。无需额外配置个人访问令牌。

## 失败与恢复

Google Scholar 没有供该脚本使用的官方 API，可能限制自动请求，参见 [scholarly 文档](https://scholarly.readthedocs.io/en/stable/quickstart.html)。抓取失败、超时或记录缺少必要信息时任务失败，原论文文件保持不变。可稍后重新运行；不以空结果覆盖现有列表。

如果论文已经提交成功、但部署启动失败，直接在 Actions 手动运行 `Deploy site`。分支保护规则如果禁止机器人直接提交，需改为审核后合并的流程；该脚本不会绕过分支保护。

本地先安装 `bin/scholar-requirements.txt` 中的依赖，然后预览：

```bash
python bin/sync_scholar_publications.py --dry-run
```

去掉 `--dry-run` 才会写入新条目。离线测试：

```bash
python -m unittest discover -s test -p 'test_scholar_sync.py'
```
