# 实例练习

## 前情回顾

- `urllib.urlopen(url[,data[,proxies]])`

> [https://docs.python.org/2/library/urllib.html](https://docs.python.org/2/library/urllib.html)

- `urllib.urlencode(query[, doseq])`

> [https://docs.python.org/2/library/urllib.html](https://docs.python.org/2/library/urllib.html)

- `urllib.FancyURLopener(...)`

> [https://docs.python.org/2/library/urllib.html](https://docs.python.org/2/library/urllib.html)

- `json.loads(s[, encoding])` 与 `json.dumps(obj, encoding="utf-8", **kw)`

> [18.2. json — JSON encoder and decoder](https://docs.python.org/2/library/json.html)

```json
{
  "current_user_url": "https://api.github.com/user",
  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
  "authorizations_url": "https://api.github.com/authorizations",
  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",
  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",
  "emails_url": "https://api.github.com/user/emails",
  "emojis_url": "https://api.github.com/emojis",
  "events_url": "https://api.github.com/events",
  "feeds_url": "https://api.github.com/feeds",
  "followers_url": "https://api.github.com/user/followers",
  "following_url": "https://api.github.com/user/following{/target}",
  "gists_url": "https://api.github.com/gists{/gist_id}",
  "hub_url": "https://api.github.com/hub",
  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
  "issues_url": "https://api.github.com/issues",
  "keys_url": "https://api.github.com/user/keys",
  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",
  "notifications_url": "https://api.github.com/notifications",
  "organization_url": "https://api.github.com/orgs/{org}",
  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
  "public_gists_url": "https://api.github.com/gists/public",
  "rate_limit_url": "https://api.github.com/rate_limit",
  "repository_url": "https://api.github.com/repos/{owner}/{repo}",
  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",
  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",
  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
  "starred_gists_url": "https://api.github.com/gists/starred",
  "user_url": "https://api.github.com/users/{user}",
  "user_organizations_url": "https://api.github.com/user/orgs",
  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"
}
```

## 挑选目标

> [https://developer.github.com/v3/](https://developer.github.com/v3/)
> [https://api.github.com/](https://api.github.com/)

### [https://api.github.com/emojis](https://api.github.com/emojis)

> [https://developer.github.com/v3/emojis/](https://developer.github.com/v3/emojis/)

- curl

```bash
$ curl https://api.github.com/emojis
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def get_github_emojis_urllib2():
    '''
    Lists all the emojis available to use on GitHub.
    '''
    response = urllib2.urlopen('https://api.github.com/emojis')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>Lists all the emojis available to use on GitHub.<<<'
    get_github_emojis_urllib2()
```

### [https://api.github.com/events](https://api.github.com/events)

> [https://developer.github.com/v3/activity/events/](https://developer.github.com/v3/activity/events/)

```bash
$ curl -I https://api.github.com/users/snowdreams1006/events
HTTP/1.1 200 OK
Date: Sat, 18 Jan 2020 14:19:42 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 56373
Server: GitHub.com
Status: 200 OK
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 1
X-RateLimit-Reset: 1579357521
Cache-Control: public, max-age=60, s-maxage=60
Vary: Accept
ETag: "45d7d76866deaf645b77be4b94dd38fa"
Last-Modified: Sat, 18 Jan 2020 14:02:11 GMT
X-Poll-Interval: 60
X-GitHub-Media-Type: github.v3; format=json
Link: <https://api.github.com/user/23238267/events?page=2>; rel="next", <https://api.github.com/user/23238267/events?page=9>; rel="last"
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type
Access-Control-Allow-Origin: *
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: deny
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy: default-src 'none'
Vary: Accept-Encoding
X-GitHub-Request-Id: 7E32:1994:2AB001:37D412:5E2313FD
```

> HTTP/1.1 200 OK
> ETag: "45d7d76866deaf645b77be4b94dd38fa"
> X-Poll-Interval: 60

```bash
# The quotes around the ETag value are important
curl -I https://api.github.com/users/snowdreams1006/events \
   -H 'If-None-Match: "45d7d76866deaf645b77be4b94dd38fa"'
HTTP/1.1 304 Not Modified
Date: Sat, 18 Jan 2020 14:23:33 GMT
Server: GitHub.com
Status: 304 Not Modified
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 1
X-RateLimit-Reset: 1579357521
Cache-Control: public, max-age=60, s-maxage=60
Vary: Accept
ETag: "45d7d76866deaf645b77be4b94dd38fa"
Last-Modified: Sat, 18 Jan 2020 14:02:11 GMT
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type
Access-Control-Allow-Origin: *
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: deny
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy: default-src 'none'
Vary: Accept-Encoding
X-GitHub-Request-Id: 7F0C:2355:2B6884:38EFF2:5E2314E3
```

> HTTP/1.1 304 Not Modified
> ETag: "45d7d76866deaf645b77be4b94dd38fa"

Link: <https://api.github.com/user/23238267/events?page=2>; rel="next", <https://api.github.com/user/23238267/events?page=9>; rel="last"

[https://api.github.com/user/23238267/events?page=9](https://api.github.com/user/23238267/events?page=9)

```bash
$ curl https://api.github.com/user/23238267/events?page=2
[
  {
    "id": "11287126905",
    "type": "IssuesEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 173099213,
      "name": "snowdreams1006/snowdreams1006.github.io",
      "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io"
    },
    "payload": {
      "action": "opened",
      "issue": {
        "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/issues/102",
        "repository_url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io",
        "labels_url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/issues/102/labels{/name}",
        "comments_url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/issues/102/comments",
        "events_url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/issues/102/events",
        "html_url": "https://github.com/snowdreams1006/snowdreams1006.github.io/issues/102",
        "id": 550547401,
        "node_id": "MDU6SXNzdWU1NTA1NDc0MDE=",
        "number": 102,
        "title": "python 学习笔记 · 雪之梦技术驿站",
        "user": {
          "login": "snowdreams1006",
          "id": 23238267,
          "node_id": "MDQ6VXNlcjIzMjM4MjY3",
          "avatar_url": "https://avatars3.githubusercontent.com/u/23238267?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/snowdreams1006",
          "html_url": "https://github.com/snowdreams1006",
          "followers_url": "https://api.github.com/users/snowdreams1006/followers",
          "following_url": "https://api.github.com/users/snowdreams1006/following{/other_user}",
          "gists_url": "https://api.github.com/users/snowdreams1006/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/snowdreams1006/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/snowdreams1006/subscriptions",
          "organizations_url": "https://api.github.com/users/snowdreams1006/orgs",
          "repos_url": "https://api.github.com/users/snowdreams1006/repos",
          "events_url": "https://api.github.com/users/snowdreams1006/events{/privacy}",
          "received_events_url": "https://api.github.com/users/snowdreams1006/received_events",
          "type": "User",
          "site_admin": false
        },
        "labels": [
          {
            "id": 1790413420,
            "node_id": "MDU6TGFiZWwxNzkwNDEzNDIw",
            "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/labels//learn-python/",
            "name": "/learn-python/",
            "color": "ededed",
            "default": false,
            "description": null
          },
          {
            "id": 1308995735,
            "node_id": "MDU6TGFiZWwxMzA4OTk1NzM1",
            "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/labels/Gitalk",
            "name": "Gitalk",
            "color": "ededed",
            "default": false,
            "description": null
          }
        ],
        "state": "open",
        "locked": false,
        "assignee": null,
        "assignees": [

        ],
        "milestone": null,
        "comments": 0,
        "created_at": "2020-01-16T03:12:11Z",
        "updated_at": "2020-01-16T03:12:11Z",
        "closed_at": null,
        "author_association": "OWNER",
        "body": "https://snowdreams1006.github.io/learn-python/ \n\n "
      }
    },
    "public": true,
    "created_at": "2020-01-16T03:12:11Z"
  },
  {
    "id": "11287093043",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4506170938,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "017552e4024800d4d4b75fb0feff735065ba7247",
      "before": "8c08ded2992b1cad6f42c47f8a40f84d0da9db7e",
      "commits": [
        {
          "sha": "017552e4024800d4d4b75fb0feff735065ba7247",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add gitlab-ci",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/017552e4024800d4d4b75fb0feff735065ba7247"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-16T03:04:18Z"
  },
  {
    "id": "11287079862",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4506163792,
      "size": 3,
      "distinct_size": 3,
      "ref": "refs/heads/master",
      "head": "8c08ded2992b1cad6f42c47f8a40f84d0da9db7e",
      "before": "1dd6344a0b4de43e0f69c3de078c95bb26936743",
      "commits": [
        {
          "sha": "666aa7915852f116cec43836d821414a182000ad",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "use_simple_urllib2_get_ip",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/666aa7915852f116cec43836d821414a182000ad"
        },
        {
          "sha": "0586c23e534fbae1746e5c69504cf499d3a464a5",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add use_simple_urllib2_get_headers",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/0586c23e534fbae1746e5c69504cf499d3a464a5"
        },
        {
          "sha": "8c08ded2992b1cad6f42c47f8a40f84d0da9db7e",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add src and docs",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/8c08ded2992b1cad6f42c47f8a40f84d0da9db7e"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-16T03:01:15Z"
  },
  {
    "id": "11279290517",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4502074312,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "1dd6344a0b4de43e0f69c3de078c95bb26936743",
      "before": "ec0b89b4e9c4138792aa2274edc511841ebb7b27",
      "commits": [
        {
          "sha": "1dd6344a0b4de43e0f69c3de078c95bb26936743",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "test imooc",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/1dd6344a0b4de43e0f69c3de078c95bb26936743"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-15T09:03:32Z"
  },
  {
    "id": "11279265810",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4502061142,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "ec0b89b4e9c4138792aa2274edc511841ebb7b27",
      "before": "170f015e7cd4012c2fe20ee799ddae76abe7c8a7",
      "commits": [
        {
          "sha": "ec0b89b4e9c4138792aa2274edc511841ebb7b27",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add main",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/ec0b89b4e9c4138792aa2274edc511841ebb7b27"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-15T09:00:25Z"
  },
  {
    "id": "11278948632",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4501893817,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "170f015e7cd4012c2fe20ee799ddae76abe7c8a7",
      "before": "bfcd611b8bbae3ba90f439a1147b198293bfc3c2",
      "commits": [
        {
          "sha": "170f015e7cd4012c2fe20ee799ddae76abe7c8a7",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add imooc-requests",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/170f015e7cd4012c2fe20ee799ddae76abe7c8a7"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-15T08:15:27Z"
  },
  {
    "id": "11278893186",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 61938302,
      "name": "jian-en/imooc-requests",
      "url": "https://api.github.com/repos/jian-en/imooc-requests"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-15T08:07:00Z"
  },
  {
    "id": "11255966510",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4489618734,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "bfcd611b8bbae3ba90f439a1147b198293bfc3c2",
      "before": "19ad5073953349315063f634bb4776f0daffcc2a",
      "commits": [
        {
          "sha": "bfcd611b8bbae3ba90f439a1147b198293bfc3c2",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add requests",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/bfcd611b8bbae3ba90f439a1147b198293bfc3c2"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-12T13:14:32Z"
  },
  {
    "id": "11255213691",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4489136473,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "19ad5073953349315063f634bb4776f0daffcc2a",
      "before": "ebc5ef354b140d583801c7ece75b029eced3d7be",
      "commits": [
        {
          "sha": "19ad5073953349315063f634bb4776f0daffcc2a",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "pip pip3",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/19ad5073953349315063f634bb4776f0daffcc2a"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-12T07:17:12Z"
  },
  {
    "id": "11255179691",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4489113955,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "ebc5ef354b140d583801c7ece75b029eced3d7be",
      "before": "028f3c69ccedce60df4f6d63db615b0f524b98ce",
      "commits": [
        {
          "sha": "ebc5ef354b140d583801c7ece75b029eced3d7be",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "which pip",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/ebc5ef354b140d583801c7ece75b029eced3d7be"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-12T06:57:36Z"
  },
  {
    "id": "11255057840",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 173099213,
      "name": "snowdreams1006/snowdreams1006.github.io",
      "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io"
    },
    "payload": {
      "push_id": 4489032742,
      "size": 2,
      "distinct_size": 2,
      "ref": "refs/heads/master",
      "head": "efef34b10339c9d92d7064180e23a43ec9b7bcde",
      "before": "80a297a05e1abc0d9420f41c5e06c639d86e49c9",
      "commits": [
        {
          "sha": "90318dc09ab9b87a33cc50e11b0f2f490ef345a7",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add novel",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/commits/90318dc09ab9b87a33cc50e11b0f2f490ef345a7"
        },
        {
          "sha": "efef34b10339c9d92d7064180e23a43ec9b7bcde",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add info",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/snowdreams1006.github.io/commits/efef34b10339c9d92d7064180e23a43ec9b7bcde"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-12T05:48:56Z"
  },
  {
    "id": "11255045723",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 1362490,
      "name": "psf/requests",
      "url": "https://api.github.com/repos/psf/requests"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-12T05:41:18Z",
    "org": {
      "id": 50630501,
      "login": "psf",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/psf",
      "avatar_url": "https://avatars.githubusercontent.com/u/50630501?"
    }
  },
  {
    "id": "11255045234",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 230031988,
      "name": "snowdreams1006/learn-python",
      "url": "https://api.github.com/repos/snowdreams1006/learn-python"
    },
    "payload": {
      "push_id": 4489024166,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "028f3c69ccedce60df4f6d63db615b0f524b98ce",
      "before": "7eb2496ef65b48e3ea0980cdaa6838a9609e6efd",
      "commits": [
        {
          "sha": "028f3c69ccedce60df4f6d63db615b0f524b98ce",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add requests",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/learn-python/commits/028f3c69ccedce60df4f6d63db615b0f524b98ce"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-12T05:41:02Z"
  },
  {
    "id": "11244357936",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 203587744,
      "name": "liyasthomas/postwoman",
      "url": "https://api.github.com/repos/liyasthomas/postwoman"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-10T06:51:34Z"
  },
  {
    "id": "11243725658",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4482614255,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "c044e8928f649f6b4fbc6c65037dc0ec2ea5784d",
      "before": "6dd3991604e1b52c311649f4d11cf52f6609f5d5",
      "commits": [
        {
          "sha": "c044e8928f649f6b4fbc6c65037dc0ec2ea5784d",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/c044e8928f649f6b4fbc6c65037dc0ec2ea5784d"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-10T04:20:10Z"
  },
  {
    "id": "11243328561",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 6662075,
      "name": "joke2k/faker",
      "url": "https://api.github.com/repos/joke2k/faker"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-10T02:40:29Z"
  },
  {
    "id": "11243204493",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 7613257,
      "name": "SeleniumHQ/selenium",
      "url": "https://api.github.com/repos/SeleniumHQ/selenium"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-10T02:10:59Z",
    "org": {
      "id": 983927,
      "login": "SeleniumHQ",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/SeleniumHQ",
      "avatar_url": "https://avatars.githubusercontent.com/u/983927?"
    }
  },
  {
    "id": "11239167728",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4480232759,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "6dd3991604e1b52c311649f4d11cf52f6609f5d5",
      "before": "6a7dd052d25e24b01ffd46731f41a742abb7321e",
      "commits": [
        {
          "sha": "6dd3991604e1b52c311649f4d11cf52f6609f5d5",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "https://12306ocr.snowdreams1006.cn/check/",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/6dd3991604e1b52c311649f4d11cf52f6609f5d5"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T15:54:36Z"
  },
  {
    "id": "11238834039",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4480058682,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "6a7dd052d25e24b01ffd46731f41a742abb7321e",
      "before": "94e84fd07670e8797e2140fc37b500e2b26269aa",
      "commits": [
        {
          "sha": "6a7dd052d25e24b01ffd46731f41a742abb7321e",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add se",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/6a7dd052d25e24b01ffd46731f41a742abb7321e"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T15:20:00Z"
  },
  {
    "id": "11236646266",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 26768643,
      "name": "SeleniumHQ/docker-selenium",
      "url": "https://api.github.com/repos/SeleniumHQ/docker-selenium"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-09T10:52:32Z",
    "org": {
      "id": 983927,
      "login": "SeleniumHQ",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/SeleniumHQ",
      "avatar_url": "https://avatars.githubusercontent.com/u/983927?"
    }
  },
  {
    "id": "11235840028",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4478485884,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "94e84fd07670e8797e2140fc37b500e2b26269aa",
      "before": "28e436157882e50cdcadcaa75c706235bd2a7314",
      "commits": [
        {
          "sha": "94e84fd07670e8797e2140fc37b500e2b26269aa",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add d",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/94e84fd07670e8797e2140fc37b500e2b26269aa"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T09:15:01Z"
  },
  {
    "id": "11235780702",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4478455100,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "28e436157882e50cdcadcaa75c706235bd2a7314",
      "before": "536df407e95841f82367fa24bd0ba74153707e08",
      "commits": [
        {
          "sha": "28e436157882e50cdcadcaa75c706235bd2a7314",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add header",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/28e436157882e50cdcadcaa75c706235bd2a7314"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T09:07:30Z"
  },
  {
    "id": "11235439459",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4478278182,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "536df407e95841f82367fa24bd0ba74153707e08",
      "before": "0b029263fcdffbcd35eb3a01429d4955993b1abc",
      "commits": [
        {
          "sha": "536df407e95841f82367fa24bd0ba74153707e08",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "        browser = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=options)",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/536df407e95841f82367fa24bd0ba74153707e08"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T08:20:26Z"
  },
  {
    "id": "11235334909",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4478223737,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "0b029263fcdffbcd35eb3a01429d4955993b1abc",
      "before": "f6f496ea74521d6b6e8c03a611253b7d963bfc06",
      "commits": [
        {
          "sha": "0b029263fcdffbcd35eb3a01429d4955993b1abc",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "userdto",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/0b029263fcdffbcd35eb3a01429d4955993b1abc"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T08:03:57Z"
  },
  {
    "id": "11234729049",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4477904672,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "f6f496ea74521d6b6e8c03a611253b7d963bfc06",
      "before": "92fc47a4f674c68635593c0104165fca195ca0be",
      "commits": [
        {
          "sha": "f6f496ea74521d6b6e8c03a611253b7d963bfc06",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add 14 users",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/f6f496ea74521d6b6e8c03a611253b7d963bfc06"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T06:15:26Z"
  },
  {
    "id": "11234084555",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4477566164,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "92fc47a4f674c68635593c0104165fca195ca0be",
      "before": "3fb726a1de56ac206e8ceec4cd4fefed96fb2672",
      "commits": [
        {
          "sha": "92fc47a4f674c68635593c0104165fca195ca0be",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add de",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/92fc47a4f674c68635593c0104165fca195ca0be"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T03:45:09Z"
  },
  {
    "id": "11234006133",
    "type": "PushEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "push_id": 4477522978,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "3fb726a1de56ac206e8ceec4cd4fefed96fb2672",
      "before": "f9a0f20e411abca79d02ed8bb1c09809f05cb9f3",
      "commits": [
        {
          "sha": "3fb726a1de56ac206e8ceec4cd4fefed96fb2672",
          "author": {
            "email": "snowdreams1006@163.com",
            "name": "snowdreams1006"
          },
          "message": "add docs modify job to save file",
          "distinct": true,
          "url": "https://api.github.com/repos/snowdreams1006/py12306/commits/3fb726a1de56ac206e8ceec4cd4fefed96fb2672"
        }
      ]
    },
    "public": true,
    "created_at": "2020-01-09T03:26:05Z"
  },
  {
    "id": "11233821842",
    "type": "WatchEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 232524279,
      "name": "snowdreams1006/py12306",
      "url": "https://api.github.com/repos/snowdreams1006/py12306"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2020-01-09T02:42:30Z"
  },
  {
    "id": "11226428928",
    "type": "ForkEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 164471183,
      "name": "pjialin/py12306",
      "url": "https://api.github.com/repos/pjialin/py12306"
    },
    "payload": {
      "forkee": {
        "id": 232524279,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMzI1MjQyNzk=",
        "name": "py12306",
        "full_name": "snowdreams1006/py12306",
        "private": false,
        "owner": {
          "login": "snowdreams1006",
          "id": 23238267,
          "node_id": "MDQ6VXNlcjIzMjM4MjY3",
          "avatar_url": "https://avatars3.githubusercontent.com/u/23238267?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/snowdreams1006",
          "html_url": "https://github.com/snowdreams1006",
          "followers_url": "https://api.github.com/users/snowdreams1006/followers",
          "following_url": "https://api.github.com/users/snowdreams1006/following{/other_user}",
          "gists_url": "https://api.github.com/users/snowdreams1006/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/snowdreams1006/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/snowdreams1006/subscriptions",
          "organizations_url": "https://api.github.com/users/snowdreams1006/orgs",
          "repos_url": "https://api.github.com/users/snowdreams1006/repos",
          "events_url": "https://api.github.com/users/snowdreams1006/events{/privacy}",
          "received_events_url": "https://api.github.com/users/snowdreams1006/received_events",
          "type": "User",
          "site_admin": false
        },
        "html_url": "https://github.com/snowdreams1006/py12306",
        "description": "🚂 12306 购票助手，支持集群，多账号，多任务购票以及 Web 页面管理 ",
        "fork": true,
        "url": "https://api.github.com/repos/snowdreams1006/py12306",
        "forks_url": "https://api.github.com/repos/snowdreams1006/py12306/forks",
        "keys_url": "https://api.github.com/repos/snowdreams1006/py12306/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/snowdreams1006/py12306/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/snowdreams1006/py12306/teams",
        "hooks_url": "https://api.github.com/repos/snowdreams1006/py12306/hooks",
        "issue_events_url": "https://api.github.com/repos/snowdreams1006/py12306/issues/events{/number}",
        "events_url": "https://api.github.com/repos/snowdreams1006/py12306/events",
        "assignees_url": "https://api.github.com/repos/snowdreams1006/py12306/assignees{/user}",
        "branches_url": "https://api.github.com/repos/snowdreams1006/py12306/branches{/branch}",
        "tags_url": "https://api.github.com/repos/snowdreams1006/py12306/tags",
        "blobs_url": "https://api.github.com/repos/snowdreams1006/py12306/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/snowdreams1006/py12306/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/snowdreams1006/py12306/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/snowdreams1006/py12306/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/snowdreams1006/py12306/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/snowdreams1006/py12306/languages",
        "stargazers_url": "https://api.github.com/repos/snowdreams1006/py12306/stargazers",
        "contributors_url": "https://api.github.com/repos/snowdreams1006/py12306/contributors",
        "subscribers_url": "https://api.github.com/repos/snowdreams1006/py12306/subscribers",
        "subscription_url": "https://api.github.com/repos/snowdreams1006/py12306/subscription",
        "commits_url": "https://api.github.com/repos/snowdreams1006/py12306/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/snowdreams1006/py12306/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/snowdreams1006/py12306/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/snowdreams1006/py12306/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/snowdreams1006/py12306/contents/{+path}",
        "compare_url": "https://api.github.com/repos/snowdreams1006/py12306/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/snowdreams1006/py12306/merges",
        "archive_url": "https://api.github.com/repos/snowdreams1006/py12306/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/snowdreams1006/py12306/downloads",
        "issues_url": "https://api.github.com/repos/snowdreams1006/py12306/issues{/number}",
        "pulls_url": "https://api.github.com/repos/snowdreams1006/py12306/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/snowdreams1006/py12306/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/snowdreams1006/py12306/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/snowdreams1006/py12306/labels{/name}",
        "releases_url": "https://api.github.com/repos/snowdreams1006/py12306/releases{/id}",
        "deployments_url": "https://api.github.com/repos/snowdreams1006/py12306/deployments",
        "created_at": "2020-01-08T09:14:16Z",
        "updated_at": "2020-01-08T09:07:10Z",
        "pushed_at": "2020-01-07T15:14:41Z",
        "git_url": "git://github.com/snowdreams1006/py12306.git",
        "ssh_url": "git@github.com:snowdreams1006/py12306.git",
        "clone_url": "https://github.com/snowdreams1006/py12306.git",
        "svn_url": "https://github.com/snowdreams1006/py12306",
        "homepage": "",
        "size": 3474,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": null,
        "has_issues": false,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "forks_count": 0,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 0,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "master",
        "public": true
      }
    },
    "public": true,
    "created_at": "2020-01-08T09:14:17Z"
  },
  {
    "id": "11226048200",
    "type": "ForkEvent",
    "actor": {
      "id": 23238267,
      "login": "snowdreams1006",
      "display_login": "snowdreams1006",
      "gravatar_id": "",
      "url": "https://api.github.com/users/snowdreams1006",
      "avatar_url": "https://avatars.githubusercontent.com/u/23238267?"
    },
    "repo": {
      "id": 195766006,
      "name": "pjialin/pyproxy-async",
      "url": "https://api.github.com/repos/pjialin/pyproxy-async"
    },
    "payload": {
      "forkee": {
        "id": 232513834,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMzI1MTM4MzQ=",
        "name": "pyproxy-async",
        "full_name": "snowdreams1006/pyproxy-async",
        "private": false,
        "owner": {
          "login": "snowdreams1006",
          "id": 23238267,
          "node_id": "MDQ6VXNlcjIzMjM4MjY3",
          "avatar_url": "https://avatars3.githubusercontent.com/u/23238267?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/snowdreams1006",
          "html_url": "https://github.com/snowdreams1006",
          "followers_url": "https://api.github.com/users/snowdreams1006/followers",
          "following_url": "https://api.github.com/users/snowdreams1006/following{/other_user}",
          "gists_url": "https://api.github.com/users/snowdreams1006/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/snowdreams1006/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/snowdreams1006/subscriptions",
          "organizations_url": "https://api.github.com/users/snowdreams1006/orgs",
          "repos_url": "https://api.github.com/users/snowdreams1006/repos",
          "events_url": "https://api.github.com/users/snowdreams1006/events{/privacy}",
          "received_events_url": "https://api.github.com/users/snowdreams1006/received_events",
          "type": "User",
          "site_admin": false
        },
        "html_url": "https://github.com/snowdreams1006/pyproxy-async",
        "description": "基于 Python Asyncio + Redis  实现的代理池",
        "fork": true,
        "url": "https://api.github.com/repos/snowdreams1006/pyproxy-async",
        "forks_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/forks",
        "keys_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/teams",
        "hooks_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/hooks",
        "issue_events_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/issues/events{/number}",
        "events_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/events",
        "assignees_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/assignees{/user}",
        "branches_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/branches{/branch}",
        "tags_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/tags",
        "blobs_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/languages",
        "stargazers_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/stargazers",
        "contributors_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/contributors",
        "subscribers_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/subscribers",
        "subscription_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/subscription",
        "commits_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/contents/{+path}",
        "compare_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/merges",
        "archive_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/downloads",
        "issues_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/issues{/number}",
        "pulls_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/labels{/name}",
        "releases_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/releases{/id}",
        "deployments_url": "https://api.github.com/repos/snowdreams1006/pyproxy-async/deployments",
        "created_at": "2020-01-08T08:19:50Z",
        "updated_at": "2020-01-08T08:19:50Z",
        "pushed_at": "2019-08-16T11:18:39Z",
        "git_url": "git://github.com/snowdreams1006/pyproxy-async.git",
        "ssh_url": "git@github.com:snowdreams1006/pyproxy-async.git",
        "clone_url": "https://github.com/snowdreams1006/pyproxy-async.git",
        "svn_url": "https://github.com/snowdreams1006/pyproxy-async",
        "homepage": "",
        "size": 87,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": null,
        "has_issues": false,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "forks_count": 0,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 0,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "master",
        "public": true
      }
    },
    "public": true,
    "created_at": "2020-01-08T08:19:51Z"
  }
]
```

#### List public events

> GET /events

- curl

```bash
$ curl https://api.github.com/events
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def list_github_public_events_urllib2():
    '''
    List public events
    '''
    response = urllib2.urlopen('https://api.github.com/events')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>List public events<<<'
    list_github_public_events_urllib2()
```

#### List repository events

> GET /repos/:owner/:repo/events

- curl

```bash
$ curl https://api.github.com/repos/snowdreams1006/learn-python/events
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def list_github_repository_events_urllib2():
    '''
    List public events
    '''
    response = urllib2.urlopen('https://api.github.com/events')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>List repository events<<<'
    list_github_repository_events_urllib2()
```

#### List issue events for a repository

> GET /repos/:owner/:repo/issues/events

- curl

```bash
$ curl https://api.github.com/repos/snowdreams1006/learn-python/issues/events
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def list_github_repository_issue_events_urllib2():
    '''
    List public events
    '''
    response = urllib2.urlopen('curl https://api.github.com/repos/snowdreams1006/learn-python/issues/events')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>List issue events for a repositorys<<<'
    list_github_repository_issue_events_urllib2()
```

#### List public events for a network of repositories

> GET /networks/:owner/:repo/events

- curl

```bash
$ curl https://api.github.com/networks/snowdreams1006/learn-python/events
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def list_github_repository_networks_events_urllib2():
    '''
    List public events for a network of repositories
    '''
    response = urllib2.urlopen('https://api.github.com/networks/snowdreams1006/learn-python/events')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>List public events for a network of repositories<<<'
    list_github_repository_networks_events_urllib2()
```

#### List public events for an organization

> GET /orgs/:org/events

- curl

```bash
$ curl https://api.github.com/orgs/python/events
```

- python

```python
# -*- coding: utf-8 -*-
import urllib2

def list_github_organization_events_urllib2():
    '''
    List public events for an organization
    '''
    response = urllib2.urlopen('https://api.github.com/orgs/python/events')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

if __name__ == '__main__':
    print '>>>List public events for an organization<<<'
    list_github_organization_events_urllib2()
```

- [https://api.github.com/feeds](https://api.github.com/feeds)
- [https://api.github.com/gists/public](https://api.github.com/gists/public)
- [https://api.github.com/rate_limit](https://api.github.com/rate_limit)

## 资源网站



## 实战练习





