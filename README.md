# java-travel-information-system
一个低级程序猿的sql作业罢了



# 基于 Java 的旅游信息管理系统的设计与实现

## 目录
1. [项目概述](#一项目概述)
2. [课题背景](#二课题背景)
3. [国内外研究现状](#三国内外研究现状)
4. [本文主要内容](#四本文主要内容)
5. [论文组织结构](#五论文组织结构)
6. [相关技术简介](#六相关技术简介)
    - [JAVA WEB 开发技术](#61-java-web-开发技术)
    - [软件体系结构](#62-软件体系结构)
    - [SQL SERVER 数据库](#63-sql-server-数据库)
7. [需求分析](#七需求分析)
    - [系统可行性研究](#71-系统可行性研究)
    - [系统需求分析](#72-系统需求分析)
    - [系统开发环境](#73-系统开发环境)
8. [系统实现](#八系统实现)
9. [测试](#九测试)
10. [总结](#十总结)
11. [致谢](#十一致谢)
12. [项目结构](#十二项目结构)
13. [参考文献](#十三参考文献)

## 一·项目概述
旅游信息管理系统是一个用于管理旅游信息资源的平台。随着旅游信息种类和数量的增加，传统的人力管理方式逐渐无法满足需求，因此开发了这个系统。系统提供了分类管理信息的功能，并以旅游信息的具体方面作为模块划分依据，旨在提高信息管理效率，节省人力物力资源。

## 二·课题背景
随着我国人们生活水平的不断提高，旅游逐渐成为人们工作之余放松压力、调节情绪的首要选择。近年来，我国旅游游客规模不断扩大，旅游业得到快速发展，但也带来了更激烈的竞争。面对更复杂的旅游业务需求，现在旅游业必须加大对当地旅游资源的宣传力度，采用更先进的技术来完成日常管理，为游客提供优质服务，帮助他们在出行时快捷、方便地查询旅游目的地的景点、酒店、交通情况。这将有助于提高城市的旅游形象和旅游服务水平。

## 三·国内外研究现状
随着计算机和网络技术的快速发展，其在社会各行各业的应用逐渐普及，越来越多的行业采用先进的计算机网络技术来管理行业信息。目前，世界范围内已有多个国家和地区成功实施了旅游信息管理系统。然而，国内旅游业的信息化进程相对缓慢，大多数城市的旅游宣传和管理方式仍以人工为主，这不仅浪费了人力和物力资源，也限制了旅游业的发展。国际上，一些发达国家已广泛使用信息管理系统来管理旅游信息，提供高度自动化和用户友好的服务平台。

## 四·本文主要内容
本文主要介绍基于 Java 技术的旅游信息管理系统的设计与实现过程。系统旨在通过现代信息技术整合和管理旅游信息资源，提高信息管理的效率，为游客提供快捷、方便的查询服务。本文分为以下几个主要部分：
1. 系统设计的背景和意义；
2. 系统需求分析；
3. 系统的总体设计；
4. 系统的详细设计与实现；
5. 系统测试与优化。

## 五·论文组织结构
本文的组织结构如下：
- 第一章：课题背景、研究现状、主要内容及论文组织结构；
- 第二章：相关技术的简介，包括 JAVA WEB 开发技术和软件体系结构；
- 第三章：需求分析，包括系统可行性研究、功能需求、性能需求及开发环境；
- 第四章：系统设计，包括系统总体设计和详细设计；
- 第五章：系统实现与测试，包括系统模块实现、数据库设计及测试方案；
- 第六章：总结与展望，概括系统的实际效果及未来发展方向。

## 六·相关技术简介

### 6.1 JAVA WEB 开发技术

#### 6.1.1 MVC 模式
MVC（Model-View-Controller）模式是一种软件设计模式，常用于创建 Web 应用。它将应用程序分为三个部分：模型（Model）、视图（View）和控制器（Controller），从而实现数据与用户界面的分离。

#### 6.1.2 J2EE 平台
J2EE（Java 2 Platform, Enterprise Edition）是 Sun Microsystems 推出的企业级计算平台。J2EE 为多层应用程序提供了一个稳定的开发和运行平台，并支持分布式、多层次的应用开发。

#### 6.1.3 SSH 框架
SSH 是 Struts、Spring、Hibernate 三个开源框架的总称。它们是 Java 企业应用开发的三个重要技术栈，分别负责表示层、业务逻辑层和持久层的开发。

#### 6.1.4 HTML 语言
HTML（HyperText Markup Language）是一种用于创建网页的标准标记语言。它通过标记文本来定义页面的结构，使得页面可以在 Web 浏览器中显示。

### 6.2 软件体系结构

#### 6.2.1 B/S 结构
B/S（Browser/Server，浏览器/服务器）结构是网络应用中一种常见的架构模式。客户端通过浏览器访问服务器，服务器处理请求并返回数据。该结构便于维护和更新应用程序，且不需要安装客户端软件。

#### 6.2.2 C/S 结构
C/S（Client/Server，客户端/服务器）结构是另一种常见的架构模式，客户端软件需要安装在用户的本地计算机上，通过网络与服务器通信。该结构多用于桌面应用和需要较高交互性的应用。

### 6.3 SQL SERVER 数据库
SQL Server 是微软开发的关系数据库管理系统，它支持多用户环境下的数据库应用。SQL Server 提供了存储、查询、更新数据的功能，并能与 .NET 平台紧密集成，为企业级应用提供强大的数据支持。

## 七·需求分析

### 7.1 系统可行性研究
在开发旅游信息管理系统之前，必须进行系统可行性研究。研究应包括技术可行性、经济可行性和操作可行性。通过这些研究，能够确定系统是否值得开发，是否符合预期目标，以及是否能够顺利实施。

### 7.2 系统需求分析

#### 7.2.1 系统实现目标
系统的主要目标是为游客提供一个全面、便捷的旅游信息查询平台，帮助他们在计划出行时能快速获取所需信息。同时，系统还需要为旅游管理者提供有效的工具，以便他们能够更好地管理和宣传当地的旅游资源。

#### 7.2.2 系统功能需求
系统需要具备的功能包括用户注册与登录、旅游景点信息的查询、旅游路线规划、酒店预订、交通信息查询、在线留言与反馈等。

#### 7.2.3 系统用例分析
系统用例分析是识别系统各部分行为的重要步骤。通过用例图，可以明确系统中不同用户的交互模式及其需要完成的任务。

#### 7.2.4 系统性能需求
系统应具备较高的响应速度，确保用户能够在较短的时间内获取所需信息。同时，系统应具备较高的可靠性和安全性，以保证数据的完整性和用户信息的安全。

### 7.3 系统开发环境
系统的开发环境包括硬件环境和软件环境。硬件环境通常包括服务器、数据库服务器及网络设备。软件环境则包括开发工具、编程语言、操作系统、数据库系统等。

## 八·系统实现

### 前台系统
首先是登陆部分：
![登录](image-32.png)

登录区分管理员与普通用户：
![管理员登录](image-33.png)

管理员登陆会直接进入管理后台：
![管理后台](image-34.png)

普通用户登录会进入个人主页：
主页中包含了线路预订与个人中心：
![个人主页](image-35.png)

主界面：
![主界面](image-31.png)

### 后台系统（管理员部分）
账号管理部分，在这里实现了管理员账户的增删查改：
![账号管理](image.png)
![账号管理2](image-1.png)

在这里实现了普通用户的增删查改以及修改密码的操作：
![用户管理](image-2.png)
![用户管理2](image-3.png)
![用户管理3](image-4.png)

地区管理部分，因为海外旅游和本地旅游现在成为一大热点，所以这里增加了境外、境内、本地三个地区。在地区管理部分实现了增删查改：
![地区管理](image-5.png)
![地区管理2](image-6.png)

在景点管理部分实现了景点的增删查改：
![景点管理](image-7.png)

对于每个景点，我们实现了景点的编辑，描述等等：
![景点编辑](image-8.png)
![景点描述](image-9.png)

在详情页面，我们可以看到景点的详情信息：
![景点详情](image-10.png)
![景点详情2](image-11.png)

在地方美食管理部分这个模块中我们分为四个部分，分别是美食分类添加查询与地方美食添加查询：
![美食管理](image-12.png)
![美食管理2](image-13.png)

地方美食添加查询部分，我们可增加美食编号，名称，附近景点分类、人均价格、美食简介等信息：
![美食添加](image-14.png)
![美食添加2](image-15.png)

通过点击information button，我们可以来到详情界面：
![详情界面](image-16.png)

甚至点击打印按钮，我们还能实现将美食信息的详情页进行打印：
![打印详情](image-17.png)

在旅游管理模块中设置了旅游线路的添加与查询：
旅游线路添加部分可以添加旅游编号、线路名称、图片、出发地、途径地、终点、价格、浏览量等信息：
![线路管理](image-18.png)

通过点击information button 我们能看到每一个路线的详情。甚至可以打印下来：
![线路详情](image-19.png)

订单预订信息的管理，可以查到每个用户的预订信息：
![订单管理](image-20.png)

新闻管理模块分为分类的添加与查询以及新闻的添加与查询：
![新闻管理](image-21.png)
![新闻管理2](image-22.png)
![新闻管理3](image-23.png)
![新闻管理4](image-24.png)

系统管理部分实现了友情链接的添加查询、轮播图的添加查询以及留言管理：
![系统管理](image-25.png)
![系统管理2](image-26.png)
![系统管理3](image-27.png)
![系统管理4](image-28.png)
![系统管理5](image-29.png)
![系统管理6](image-30.png)

### 后台系统（普通用户部分）
线路预订管理：
![线路预订](image-36.png)

个人中心的管理包括了 修改个人资料，修改密码，我的收藏，我的留言部分：
![个人中心](image-37.png)

## 九·测试
系统测试包括单元测试、集成测试和系统测试，目的是在软件投入运行前尽可能多地发现错误，确保软件质量。

## 十·总结
通过系统开发，提高了对系统分析、数据流图、数据字典等系统设计工具的认识，积累了宝贵的经验。

## 十一·致谢
感谢学校和指导老师在设计过程中的帮助和建议，使系统开发水平得到了提高。

## 十二·项目结构
```plaintext
.
├── LICENSE
├── README.md
├── bysj-client1
│   ├── babel.config.js
│   ├── node_modules
│   │   ├── @achrinza
│   │   ├── @ampproject
│   │   ├── @babel
│   │   ├── @hapi
│   │   ├── @intervolga
│   │   ├── @jridgewell
│   │   ├── @mrmlnc
│   │   ├── @node-ipc
│   │   ├── @nodelib
│   │   ├── @riophae
│   │   ├── @sideway
│   │   ├── @soda
│   │   ├── @types
│   │   ├── @videojs
│   │   ├── @vue
│   │   ├── @webassemblyjs
│   │   ├── @xmldom
│   │   ├── @xtuc
│   │   ├── accepts
│   │   ├── acorn
│   │   ├── acorn-jsx
│   │   ├── acorn-walk
│   │   ├── add-dom-event-listener
│   │   ├── address
│   │   ├── aes-decrypter
│   │   ├── ajv
│   │   ├── ajv-errors
│   │   ├── ajv-formats
│   │   ├── ajv-keywords
│   │   ├── alphanum-sort
│   │   ├── ansi-colors
│   │   ├── ansi-escapes
│   │   ├── ansi-html-community
│   │   ├── ansi-regex
│   │   ├── ansi-styles
│   │   ├── any-promise
│   │   ├── anymatch
│   │   ├── aproba
│   │   ├── arch
│   │   ├── argparse
│   │   ├── arr-diff
│   │   ├── arr-flatten
│   │   ├── arr-union
│   │   ├── array-buffer-byte-length
│   │   ├── array-flatten
│   │   ├── array-union
│   │   ├── array-uniq
│   │   ├── array-unique
│   │   ├── array.prototype.reduce
│   │   ├── arraybuffer.prototype.slice
│   │   ├── asn1
│   │   ├── asn1.js
│   │   ├── assert
│   │   ├── assert-plus
│   │   ├── assign-symbols
│   │   ├── astral-regex
│   │   ├── async
│   │   ├── async-each
│   │   ├── async-limiter
│   │   ├── async-validator
│   │   ├── asynckit
│   │   ├── atob
│   │   ├── autoprefixer
│   │   ├── available-typed-arrays
│   │   ├── aws-sign2
│   │   ├── aws4
│   │   ├── axios
│   │   ├── babel-eslint
│   │   ├── babel-helper-vue-jsx-merge-props
│   │   ├── babel-loader
│   │   ├── babel-plugin-dynamic-import-node
│   │   ├── babel-plugin-polyfill-corejs2
│   │   ├── babel-plugin-polyfill-corejs3
│   │   ├── babel-plugin-polyfill-regenerator
│   │   ├── babel-runtime
│   │   ├── balanced-match
│   │   ├── base
│   │   ├── base64-js
│   │   ├── batch
│   │   ├── bcrypt-pbkdf
│   │   ├── bfj
│   │   ├── big.js
│   │   ├── binary-extensions
│   │   ├── bindings
│   │   ├── bl
│   │   ├── bluebird
│   │   ├── bmaplib.curveline
│   │   ├── bmaplib.heatmap
│   │   ├── bmaplib.lushu
│   │   ├── bmaplib.markerclusterer
│   │   ├── bmaplib.texticonoverlay
│   │   ├── bn.js
│   │   ├── body-parser
│   │   ├── bonjour
│   │   ├── boolbase
│   │   ├── brace-expansion
│   │   ├── braces
│   │   ├── brorand
│   │   ├── browserify-aes
│   │   ├── browserify-cipher
│   │   ├── browserify-des
│   │   ├── browserify-rsa
│   │   ├── browserify-sign
│   │   ├── browserify-zlib
│   │   ├── browserslist
│   │   ├── buffer
│   │   ├── buffer-from
│   │   ├── buffer-indexof
│   │   ├── buffer-json
│   │   ├── buffer-xor
│   │   ├── builtin-status-codes
│   │   ├── bytes
│   │   ├── cacache
│   │   ├── cache-base
│   │   ├── cache-loader
│   │   ├── call-bind
│   │   ├── call-me-maybe
│   │   ├── caller-callsite
│   │   ├── caller-path
│   │   ├── callsites
│   │   ├── camel-case
│   │   ├── camelcase
│   │   ├── caniuse-api
│   │   ├── caniuse-lite
│   │   ├── case-sensitive-paths-webpack-plugin
│   │   ├── caseless
│   │   ├── chalk
│   │   ├── chardet
│   │   ├── check-types
│   │   ├── chokidar
│   │   ├── chownr
│   │   ├── chrome-trace-event
│   │   ├── ci-info
│   │   ├── cipher-base
│   │   ├── class-utils
│   │   ├── clean-css
│   │   ├── cli-cursor
│   │   ├── cli-highlight
│   │   ├── cli-spinners
│   │   ├── cli-width
│   │   ├── clipboardy
│   │   ├── cliui
│   │   ├── clone
│   │   ├── coa
│   │   ├── collection-visit
│   │   ├── color
│   │   ├── color-convert
│   │   ├── color-name
│   │   ├── color-string
│   │   ├── combined-stream
│   │   ├── commander
│   │   ├── commondir
│   │   ├── component-emitter
│   │   ├── compressible
│   │   ├── compression
│   │   ├── concat-map
│   │   ├── concat-stream
│   │   ├── connect-history-api-fallback
│   │   ├── console-browserify
│   │   ├── consolidate
│   │   ├── constants-browserify
│   │   ├── content-disposition
│   │   ├── content-type
│   │   ├── convert-source-map
│   │   ├── cookie
│   │   ├── cookie-signature
│   │   ├── copy-concurrently
│   │   ├── copy-descriptor
│   │   ├── copy-webpack-plugin
│   │   ├── core-js
│   │   ├── core-js-compat
│   │   ├── core-util-is
│   │   ├── cosmiconfig
│   │   ├── create-ecdh
│   │   ├── create-hash
│   │   ├── create-hmac
│   │   ├── cross-spawn
│   │   ├── crypto-browserify
│   │   ├── css-color-names
│   │   ├── css-declaration-sorter
│   │   ├── css-loader
│   │   ├── css-select
│   │   ├── css-select-base-adapter
│   │   ├── css-tree
│   │   ├── css-what
│   │   ├── cssesc
│   │   ├── cssnano
│   │   ├── cssnano-preset-default
│   │   ├── cssnano-util-get-arguments
│   │   ├── cssnano-util-get-match
│   │   ├── cssnano-util-raw-cache
│   │   ├── cssnano-util-same-parent
│   │   ├── csso
│   │   ├── csstype
│   │   ├── cyclist
│   │   ├── dashdash
│   │   ├── de-indent
│   │   ├── debug
│   │   ├── decamelize
│   │   ├── decode-uri-component
│   │   ├── deep-equal
│   │   ├── deep-is
│   │   ├── deepmerge
│   │   ├── default-gateway
│   │   ├── defaults
│   │   ├── define-data-property
│   │   ├── define-lazy-prop
│   │   ├── define-properties
│   │   ├── define-property
│   │   ├── del
│   │   ├── delayed-stream
│   │   ├── depd
│   │   ├── des.js
│   │   ├── destroy
│   │   ├── detect-node
│   │   ├── diffie-hellman
│   │   ├── dir-glob
│   │   ├── dns-equal
│   │   ├── dns-packet
│   │   ├── dns-txt
│   │   ├── doctrine
│   │   ├── dom-converter
│   │   ├── dom-serializer
│   │   ├── dom-walk
│   │   ├── domain-browser
│   │   ├── domelementtype
│   │   ├── domhandler
│   │   ├── domutils
│   │   ├── dot-prop
│   │   ├── dotenv
│   │   ├── dotenv-expand
│   │   ├── duplexer
│   │   ├── duplexify
│   │   ├── easings-css
│   │   ├── easy-stack
│   │   ├── ecc-jsbn
│   │   ├── ee-first
│   │   ├── ejs
│   │   ├── electron-to-chromium
│   │   ├── element-ui
│   │   ├── elliptic
│   │   ├── emoji-regex
│   │   ├── emojis-list
│   │   ├── encodeurl
│   │   ├── end-of-stream
│   │   ├── enhanced-resolve
│   │   ├── errno
│   │   ├── error-ex
│   │   ├── error-stack-parser
│   │   ├── es-abstract
│   │   ├── es-array-method-boxes-properly
│   │   ├── es-module-lexer
│   │   ├── es-set-tostringtag
│   │   ├── es-to-primitive
│   │   ├── escalade
│   │   ├── escape-html
│   │   ├── escape-string-regexp
│   │   ├── eslint
│   │   ├── eslint-plugin-vue
│   │   ├── eslint-scope
│   │   ├── eslint-utils
│   │   ├── eslint-visitor-keys
│   │   ├── espree
│   │   ├── esprima
│   │   ├── esquery
│   │   ├── esrecurse
│   │   ├── estraverse
│   │   ├── estree-walker
│   │   ├── esutils
│   │   ├── etag
│   │   ├── event-pubsub
│   │   ├── eventemitter3
│   │   ├── events
│   │   ├── eventsource
│   │   ├── evp_bytestokey
│   │   ├── execa
│   │   ├── expand-brackets
│   │   ├── express
│   │   ├── extend
│   │   ├── extend-shallow
│   │   ├── external-editor
│   │   ├── extglob
│   │   ├── extsprintf
│   │   ├── fast-deep-equal
│   │   ├── fast-glob
│   │   ├── fast-json-stable-stringify
│   │   ├── fast-levenshtein
│   │   ├── fast-uri
│   │   ├── fastq
│   │   ├── faye-websocket
│   │   ├── figgy-pudding
│   │   ├── figures
│   │   ├── file-entry-cache
│   │   ├── file-loader
│   │   ├── file-uri-to-path
│   │   ├── filesize
│   │   ├── fill-range
│   │   ├── finalhandler
│   │   ├── find-cache-dir
│   │   ├── find-up
│   │   ├── flat-cache
│   │   ├── flatted
│   │   ├── flush-write-stream
│   │   ├── follow-redirects
│   │   ├── font-awesome
│   │   ├── for-each
│   │   ├── for-in
│   │   ├── forever-agent
│   │   ├── form-data
│   │   ├── forwarded
│   │   ├── fragment-cache
│   │   ├── fresh
│   │   ├── from2
│   │   ├── fs-extra
│   │   ├── fs-write-stream-atomic
│   │   ├── fs.realpath
│   │   ├── fsevents
│   │   ├── function-bind
│   │   ├── function.prototype.name
│   │   ├── functional-red-black-tree
│   │   ├── functions-have-names
│   │   ├── fuzzysearch
│   │   ├── gensync
│   │   ├── get-caller-file
│   │   ├── get-intrinsic
│   │   ├── get-stream
│   │   ├── get-symbol-description
│   │   ├── get-value
│   │   ├── getpass
│   │   ├── glob
│   │   ├── glob-parent
│   │   ├── glob-to-regexp
│   │   ├── global
│   │   ├── globals
│   │   ├── globalthis
│   │   ├── globby
│   │   ├── gopd
│   │   ├── graceful-fs
│   │   ├── gzip-size
│   │   ├── handle-thing
│   │   ├── har-schema
│   │   ├── har-validator
│   │   ├── has
│   │   ├── has-bigints
│   │   ├── has-flag
│   │   ├── has-property-descriptors
│   │   ├── has-proto
│   │   ├── has-symbols
│   │   ├── has-tostringtag
│   │   ├── has-value
│   │   ├── has-values
│   │   ├── hash-base
│   │   ├── hash-sum
│   │   ├── hash.js
│   │   ├── hasown
│   │   ├── he
│   │   ├── hex-color-regex
│   │   ├── highlight.js
│   │   ├── hmac-drbg
│   │   ├── hoopy
│   │   ├── hosted-git-info
│   │   ├── hpack.js
│   │   ├── hsl-regex
│   │   ├── hsla-regex
│   │   ├── html-entities
│   │   ├── html-minifier
│   │   ├── html-tags
│   │   ├── html-webpack-plugin
│   │   ├── htmlparser2
│   │   ├── http-deceiver
│   │   ├── http-errors
│   │   ├── http-parser-js
│   │   ├── http-proxy
│   │   ├── http-proxy-middleware
│   │   ├── http-signature
│   │   ├── https-browserify
│   │   ├── human-signals
│   │   ├── iconv-lite
│   │   ├── icss-utils
│   │   ├── ieee754
│   │   ├── iferr
│   │   ├── ignore
│   │   ├── immutable
│   │   ├── import-cwd
│   │   ├── import-fresh
│   │   ├── import-from
│   │   ├── import-local
│   │   ├── imurmurhash
│   │   ├── indexes-of
│   │   ├── individual
│   │   ├── infer-owner
│   │   ├── inflight
│   │   ├── inherits
│   │   ├── inquirer
│   │   ├── internal-ip
│   │   ├── internal-slot
│   │   ├── ip
│   │   ├── ip-regex
│   │   ├── ipaddr.js
│   │   ├── is-absolute-url
│   │   ├── is-accessor-descriptor
│   │   ├── is-arguments
│   │   ├── is-array-buffer
│   │   ├── is-arrayish
│   │   ├── is-bigint
│   │   ├── is-binary-path
│   │   ├── is-boolean-object
│   │   ├── is-buffer
│   │   ├── is-callable
│   │   ├── is-ci
│   │   ├── is-color-stop
│   │   ├── is-core-module
│   │   ├── is-data-descriptor
│   │   ├── is-date-object
│   │   ├── is-descriptor
│   │   ├── is-directory
│   │   ├── is-docker
│   │   ├── is-extendable
│   │   ├── is-extglob
│   │   ├── is-fullwidth-code-point
│   │   ├── is-function
│   │   ├── is-glob
│   │   ├── is-interactive
│   │   ├── is-negative-zero
│   │   ├── is-number
│   │   ├── is-number-object
│   │   ├── is-obj
│   │   ├── is-path-cwd
│   │   ├── is-path-in-cwd
│   │   ├── is-path-inside
│   │   ├── is-plain-obj
│   │   ├── is-plain-object
│   │   ├── is-promise
│   │   ├── is-regex
│   │   ├── is-resolvable
│   │   ├── is-shared-array-buffer
│   │   ├── is-stream
│   │   ├── is-string
│   │   ├── is-symbol
│   │   ├── is-typed-array
│   │   ├── is-typedarray
│   │   ├── is-unicode-supported
│   │   ├── is-weakref
│   │   ├── is-windows
│   │   ├── is-wsl
│   │   ├── isarray
│   │   ├── isexe
│   │   ├── isobject
│   │   ├── isstream
│   │   ├── javascript-stringify
│   │   ├── jest-worker
│   │   ├── joi
│   │   ├── js-message
│   │   ├── js-tokens
│   │   ├── js-yaml
│   │   ├── jsbn
│   │   ├── jsesc
│   │   ├── json-parse-better-errors
│   │   ├── json-parse-even-better-errors
│   │   ├── json-schema
│   │   ├── json-schema-traverse
│   │   ├── json-stable-stringify-without-jsonify
│   │   ├── json-stringify-safe
│   │   ├── json5
│   │   ├── jsonfile
│   │   ├── jsprim
│   │   ├── keycode
│   │   ├── killable
│   │   ├── kind-of
│   │   ├── klona
│   │   ├── launch-editor
│   │   ├── launch-editor-middleware
│   │   ├── levn
│   │   ├── lines-and-columns
│   │   ├── loader-runner
│   │   ├── loader-utils
│   │   ├── locate-path
│   │   ├── lodash
│   │   ├── lodash.debounce
│   │   ├── lodash.defaultsdeep
│   │   ├── lodash.kebabcase
│   │   ├── lodash.mapvalues
│   │   ├── lodash.memoize
│   │   ├── lodash.transform
│   │   ├── lodash.uniq
│   │   ├── log-symbols
│   │   ├── loglevel
│   │   ├── lower-case
│   │   ├── lru-cache
│   │   ├── m3u8-parser
│   │   ├── magic-string
│   │   ├── make-dir
│   │   ├── map-cache
│   │   ├── map-visit
│   │   ├── material-colors
│   │   ├── md5.js
│   │   ├── mdn-data
│   │   ├── media-typer
│   │   ├── memory-fs
│   │   ├── merge-descriptors
│   │   ├── merge-source-map
│   │   ├── merge-stream
│   │   ├── merge2
│   │   ├── methods
│   │   ├── micromatch
│   │   ├── miller-rabin
│   │   ├── mime
│   │   ├── mime-db
│   │   ├── mime-types
│   │   ├── mimic-fn
│   │   ├── min-document
│   │   ├── mini-css-extract-plugin
│   │   ├── minimalistic-assert
│   │   ├── minimalistic-crypto-utils
│   │   ├── minimatch
│   │   ├── minimist
│   │   ├── minipass
│   │   ├── mississippi
│   │   ├── mixin-deep
│   │   ├── mkdirp
│   │   ├── move-concurrently
│   │   ├── mpd-parser
│   │   ├── ms
│   │   ├── multicast-dns
│   │   ├── multicast-dns-service-types
│   │   ├── mute-stream
│   │   ├── mux.js
│   │   ├── mz
│   │   ├── nan
│   │   ├── nanoid
│   │   ├── nanomatch
│   │   ├── natural-compare
│   │   ├── negotiator
│   │   ├── neo-async
│   │   ├── nice-try
│   │   ├── no-case
│   │   ├── node-fetch
│   │   ├── node-forge
│   │   ├── node-libs-browser
│   │   ├── node-releases
│   │   ├── normalize-package-data
│   │   ├── normalize-path
│   │   ├── normalize-range
│   │   ├── normalize-url
│   │   ├── normalize-wheel
│   │   ├── normalize.css
│   │   ├── npm-run-path
│   │   ├── nprogress
│   │   ├── nth-check
│   │   ├── num2fraction
│   │   ├── oauth-sign
│   │   ├── object-assign
│   │   ├── object-copy
│   │   ├── object-inspect
│   │   ├── object-is
│   │   ├── object-keys
│   │   ├── object-visit
│   │   ├── object.assign
│   │   ├── object.getownpropertydescriptors
│   │   ├── object.pick
│   │   ├── object.values
│   │   ├── objectdiff
│   │   ├── obuf
│   │   ├── on-finished
│   │   ├── on-headers
│   │   ├── once
│   │   ├── onetime
│   │   ├── open
│   │   ├── opener
│   │   ├── opn
│   │   ├── optionator
│   │   ├── ora
│   │   ├── os-browserify
│   │   ├── os-tmpdir
│   │   ├── p-finally
│   │   ├── p-limit
│   │   ├── p-locate
│   │   ├── p-map
│   │   ├── p-retry
│   │   ├── p-try
│   │   ├── pako
│   │   ├── parallel-transform
│   │   ├── param-case
│   │   ├── parent-module
│   │   ├── parse-asn1
│   │   ├── parse-json
│   │   ├── parse5
│   │   ├── parse5-htmlparser2-tree-adapter
│   │   ├── parseurl
│   │   ├── pascalcase
│   │   ├── path-browserify
│   │   ├── path-dirname
│   │   ├── path-exists
│   │   ├── path-is-absolute
│   │   ├── path-is-inside
│   │   ├── path-key
│   │   ├── path-parse
│   │   ├── path-to-regexp
│   │   ├── path-type
│   │   ├── pbkdf2
│   │   ├── performance-now
│   │   ├── picocolors
│   │   ├── picomatch
│   │   ├── pify
│   │   ├── pinkie
│   │   ├── pinkie-promise
│   │   ├── pkcs7
│   │   ├── pkg-dir
│   │   ├── pnp-webpack-plugin
│   │   ├── portfinder
│   │   ├── posix-character-classes
│   │   ├── postcss
│   │   ├── postcss-calc
│   │   ├── postcss-colormin
│   │   ├── postcss-convert-values
│   │   ├── postcss-discard-comments
│   │   ├── postcss-discard-duplicates
│   │   ├── postcss-discard-empty
│   │   ├── postcss-discard-overridden
│   │   ├── postcss-load-config
│   │   ├── postcss-loader
│   │   ├── postcss-merge-longhand
│   │   ├── postcss-merge-rules
│   │   ├── postcss-minify-font-values
│   │   ├── postcss-minify-gradients
│   │   ├── postcss-minify-params
│   │   ├── postcss-minify-selectors
│   │   ├── postcss-modules-extract-imports
│   │   ├── postcss-modules-local-by-default
│   │   ├── postcss-modules-scope
│   │   ├── postcss-modules-values
│   │   ├── postcss-normalize-charset
│   │   ├── postcss-normalize-display-values
│   │   ├── postcss-normalize-positions
│   │   ├── postcss-normalize-repeat-style
│   │   ├── postcss-normalize-string
│   │   ├── postcss-normalize-timing-functions
│   │   ├── postcss-normalize-unicode
│   │   ├── postcss-normalize-url
│   │   ├── postcss-normalize-whitespace
│   │   ├── postcss-ordered-values
│   │   ├── postcss-reduce-initial
│   │   ├── postcss-reduce-transforms
│   │   ├── postcss-selector-parser
│   │   ├── postcss-svgo
│   │   ├── postcss-unique-selectors
│   │   ├── postcss-value-parser
│   │   ├── prelude-ls
│   │   ├── prepend-http
│   │   ├── prettier
│   │   ├── pretty-error
│   │   ├── process
│   │   ├── process-nextick-args
│   │   ├── progress
│   │   ├── promise-inflight
│   │   ├── proxy-addr
│   │   ├── proxy-from-env
│   │   ├── prr
│   │   ├── pseudomap
│   │   ├── psl
│   │   ├── public-encrypt
│   │   ├── pump
│   │   ├── pumpify
│   │   ├── punycode
│   │   ├── q
│   │   ├── qs
│   │   ├── query-string
│   │   ├── querystring-es3
│   │   ├── querystringify
│   │   ├── queue-microtask
│   │   ├── randombytes
│   │   ├── randomfill
│   │   ├── range-parser
│   │   ├── raw-body
│   │   ├── read-pkg
│   │   ├── readable-stream
│   │   ├── readdirp
│   │   ├── regenerate
│   │   ├── regenerate-unicode-properties
│   │   ├── regenerator-runtime
│   │   ├── regenerator-transform
│   │   ├── regex-not
│   │   ├── regexp.prototype.flags
│   │   ├── regexpp
│   │   ├── regexpu-core
│   │   ├── regjsparser
│   │   ├── relateurl
│   │   ├── remove-trailing-separator
│   │   ├── renderkid
│   │   ├── repeat-element
│   │   ├── repeat-string
│   │   ├── request
│   │   ├── require-directory
│   │   ├── require-from-string
│   │   ├── require-main-filename
│   │   ├── requires-port
│   │   ├── resize-observer-polyfill
│   │   ├── resolve
│   │   ├── resolve-cwd
│   │   ├── resolve-from
│   │   ├── resolve-url
│   │   ├── restore-cursor
│   │   ├── ret
│   │   ├── retry
│   │   ├── reusify
│   │   ├── rgb-regex
│   │   ├── rgba-regex
│   │   ├── rimraf
│   │   ├── ripemd160
│   │   ├── run-async
│   │   ├── run-parallel
│   │   ├── run-queue
│   │   ├── rust-result
│   │   ├── rxjs
│   │   ├── safe-array-concat
│   │   ├── safe-buffer
│   │   ├── safe-json-parse
│   │   ├── safe-regex
│   │   ├── safe-regex-test
│   │   ├── safer-buffer
│   │   ├── sass
│   │   ├── sass-loader
│   │   ├── sax
│   │   ├── schema-utils
│   │   ├── select-hose
│   │   ├── selfsigned
│   │   ├── semver
│   │   ├── send
│   │   ├── serialize-javascript
│   │   ├── serve-index
│   │   ├── serve-static
│   │   ├── set-blocking
│   │   ├── set-function-length
│   │   ├── set-function-name
│   │   ├── set-value
│   │   ├── setimmediate
│   │   ├── setprototypeof
│   │   ├── sha.js
│   │   ├── shebang-command
│   │   ├── shebang-regex
│   │   ├── shell-quote
│   │   ├── side-channel
│   │   ├── signal-exit
│   │   ├── simple-swizzle
│   │   ├── slash
│   │   ├── slice-ansi
│   │   ├── snapdragon
│   │   ├── snapdragon-node
│   │   ├── snapdragon-util
│   │   ├── sockjs
│   │   ├── sockjs-client
│   │   ├── sort-keys
│   │   ├── sortablejs
│   │   ├── source-list-map
│   │   ├── source-map
│   │   ├── source-map-js
│   │   ├── source-map-resolve
│   │   ├── source-map-support
│   │   ├── source-map-url
│   │   ├── spdx-correct
│   │   ├── spdx-exceptions
│   │   ├── spdx-expression-parse
│   │   ├── spdx-license-ids
│   │   ├── spdy
│   │   ├── spdy-transport
│   │   ├── split-string
│   │   ├── sprintf-js
│   │   ├── sshpk
│   │   ├── ssri
│   │   ├── stable
│   │   ├── stackframe
│   │   ├── static-extend
│   │   ├── statuses
│   │   ├── stream-browserify
│   │   ├── stream-each
│   │   ├── stream-http
│   │   ├── stream-shift
│   │   ├── strict-uri-encode
│   │   ├── string-width
│   │   ├── string.prototype.trim
│   │   ├── string.prototype.trimend
│   │   ├── string.prototype.trimstart
│   │   ├── string_decoder
│   │   ├── strip-ansi
│   │   ├── strip-eof
│   │   ├── strip-final-newline
│   │   ├── strip-indent
│   │   ├── strip-json-comments
│   │   ├── stylehacks
│   │   ├── supports-color
│   │   ├── supports-preserve-symlinks-flag
│   │   ├── svg-tags
│   │   ├── svgo
│   │   ├── table
│   │   ├── tapable
│   │   ├── terser
│   │   ├── terser-webpack-plugin
│   │   ├── text-table
│   │   ├── thenify
│   │   ├── thenify-all
│   │   ├── thread-loader
│   │   ├── throttle-debounce
│   │   ├── through
│   │   ├── through2
│   │   ├── thunky
│   │   ├── timers-browserify
│   │   ├── timsort
│   │   ├── tmp
│   │   ├── to-arraybuffer
│   │   ├── to-fast-properties
│   │   ├── to-object-path
│   │   ├── to-regex
│   │   ├── to-regex-range
│   │   ├── toidentifier
│   │   ├── toposort
│   │   ├── tough-cookie
│   │   ├── tr46
│   │   ├── tryer
│   │   ├── ts-pnp
│   │   ├── tslib
│   │   ├── tty-browserify
│   │   ├── tunnel-agent
│   │   ├── tweetnacl
│   │   ├── type-check
│   │   ├── type-fest
│   │   ├── type-is
│   │   ├── typed-array-buffer
│   │   ├── typed-array-byte-length
│   │   ├── typed-array-byte-offset
│   │   ├── typed-array-length
│   │   ├── typedarray
│   │   ├── uglify-js
│   │   ├── unbox-primitive
│   │   ├── undici-types
│   │   ├── unicode-canonical-property-names-ecmascript
│   │   ├── unicode-match-property-ecmascript
│   │   ├── unicode-match-property-value-ecmascript
│   │   ├── unicode-property-aliases-ecmascript
│   │   ├── union-value
│   │   ├── uniq
│   │   ├── uniqs
│   │   ├── unique-filename
│   │   ├── unique-slug
│   │   ├── universalify
│   │   ├── unpipe
│   │   ├── unquote
│   │   ├── unset-value
│   │   ├── upath
│   │   ├── update-browserslist-db
│   │   ├── upper-case
│   │   ├── uri-js
│   │   ├── urix
│   │   ├── url
│   │   ├── url-loader
│   │   ├── url-parse
│   │   ├── url-toolkit
│   │   ├── use
│   │   ├── util
│   │   ├── util-deprecate
│   │   ├── util.promisify
│   │   ├── utila
│   │   ├── utils-merge
│   │   ├── uuid
│   │   ├── v-viewer
│   │   ├── v8-compile-cache
│   │   ├── validate-npm-package-license
│   │   ├── vary
│   │   ├── vendors
│   │   ├── verror
│   │   ├── video.js
│   │   ├── videojs-font
│   │   ├── videojs-vtt.js
│   │   ├── viewerjs
│   │   ├── vm-browserify
│   │   ├── vue
│   │   ├── vue-baidu-map
│   │   ├── vue-cli-plugin-element-ui
│   │   ├── vue-eslint-parser
│   │   ├── vue-hot-reload-api
│   │   ├── vue-loader
│   │   ├── vue-loader-v16
│   │   ├── vue-router
│   │   ├── vue-style-loader
│   │   ├── vue-template-compiler
│   │   ├── vue-template-es2015-compiler
│   │   ├── vue-video-player
│   │   ├── vuedraggable
│   │   ├── vuex
│   │   ├── watch-size
│   │   ├── watchpack
│   │   ├── watchpack-chokidar2
│   │   ├── wbuf
│   │   ├── wcwidth
│   │   ├── webidl-conversions
│   │   ├── webpack
│   │   ├── webpack-bundle-analyzer
│   │   ├── webpack-chain
│   │   ├── webpack-dev-middleware
│   │   ├── webpack-dev-server
│   │   ├── webpack-log
│   │   ├── webpack-merge
│   │   ├── webpack-sources
│   │   ├── websocket-driver
│   │   ├── websocket-extensions
│   │   ├── whatwg-url
│   │   ├── which
│   │   ├── which-boxed-primitive
│   │   ├── which-module
│   │   ├── which-typed-array
│   │   ├── word-wrap
│   │   ├── worker-farm
│   │   ├── wrap-ansi
│   │   ├── wrappy
│   │   ├── write
│   │   ├── ws
│   │   ├── xtend
│   │   ├── y18n
│   │   ├── yallist
│   │   ├── yargs
│   │   ├── yargs-parser
│   │   └── yorkie
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   └── static
│   ├── src
│   │   ├── App.vue
│   │   ├── api.js
│   │   ├── assets
│   │   ├── components
│   │   ├── config.js
│   │   ├── main.js
│   │   ├── router
│   │   ├── setting.js
│   │   ├── store
│   │   ├── styles.scss
│   │   ├── utils
│   │   └── views
│   ├── test
│   │   ├── README.md
│   │   ├── index.html
│   │   ├── jsconfig.json
│   │   ├── node_modules
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   ├── public
│   │   ├── src
│   │   └── vite.config.js
│   ├── test.iml
│   ├── vue.config.js
│   └── webpack.config.js
├── bysj-server
│   ├── D:\maven\mvn-repository
│   │   ├── antlr
│   │   ├── aopalliance
│   │   ├── asm
│   │   ├── avalon-framework
│   │   ├── backport-util-concurrent
│   │   ├── ch
│   │   ├── classworlds
│   │   ├── com
│   │   ├── commons-beanutils
│   │   ├── commons-chain
│   │   ├── commons-codec
│   │   ├── commons-collections
│   │   ├── commons-digester
│   │   ├── commons-fileupload
│   │   ├── commons-io
│   │   ├── commons-lang
│   │   ├── commons-logging
│   │   ├── commons-validator
│   │   ├── dom4j
│   │   ├── io
│   │   ├── javax
│   │   ├── junit
│   │   ├── log4j
│   │   ├── logkit
│   │   ├── mysql
│   │   ├── net
│   │   ├── org
│   │   ├── oro
│   │   ├── sslext
│   │   ├── tk
│   │   └── xml-apis
│   ├── HELP.md
│   ├── WEB-INF
│   │   └── web.xml
│   ├── bysj-server.iml
│   ├── database
│   │   └── spbootvue07987lyxxtjxtsjysx.sql
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── out
│   │   └── artifacts
│   ├── package-lock.json
│   ├── pom.xml
│   ├── src
│   │   └── main
│   ├── target
│   │   ├── BOOT-INF
│   │   ├── classes
│   │   ├── generated-sources
│   │   ├── maven-archiver
│   │   ├── maven-status
│   │   ├── travel-0.0.1-SNAPSHOT.jar
│   │   └── travel-0.0.1-SNAPSHOT.jar.original
│   └── 数据库表结构.doc
├── project-structure.txt
└── 数据库文件
    └── spbootvue07987.sql

983 directories, 35 files
```


## 参考文献
1. Todd Cook. JSP从入门到精通[M]. 北京：电子工业出版社，2003.
2. Soren Lauesen. Software Requirements Styles and Techniques[M]. 北京：电子工业出版社，2002.
3. Roger S. Pressman. Software Engineering A Practitioner’s Approach 5th ed[M]. 北京：清华大学出版社，2001.
4. Hans Bergsten. JavaServer Pages_2nd Edition[M]. O'Reilly, 2002.
5. Kevin Duffey, Vikram Goyal. Professional JSP Site Design[M]. 北京：电子工业出版社，2002.
6. Paul C. Jorgensen. Software Testing A Craftsman’s Approach (second Edition)[M]. China Machine Press, 2003.
