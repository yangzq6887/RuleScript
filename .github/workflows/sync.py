import gitlab

# GitLab 仓库信息
gitlab_url = 'https://gitlab.com/yangzq106/rulescript.git'
gitlab_token = 'glpat-_65j-ECaCJZGeXkDqk74'

# 克隆 GitHub 仓库
git_repo = git.Repo.clone_from('https://github.com/blackmatrix7/ios_rule_script.git', 'ios_rule_script')

# 检查更新
origin = git_repo.remotes.origin
origin.fetch()
if origin.refs.master.commit.hexsha != git_repo.head.commit.hexsha:
    # 有更新，同步到 GitLab
    gitlab_client = gitlab.Gitlab(gitlab_url, private_token=gitlab_token)
    gitlab_repo = gitlab_client.get_project('new-repo')
    gitlab_repo.remotes.create({'url': 'https://github.com/blackmatrix7/ios_rule_script.git', 'name': 'github'})
    gitlab_repo.push('master', remote_name='github')

