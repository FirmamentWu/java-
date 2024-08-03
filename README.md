# java-travel-information-system
一个低级程序猿的sql作业罢了


# 旅游信息管理系统

## 一·项目概述
旅游信息管理系统是一个用于管理旅游信息资源的平台。随着旅游信息种类和数量的增加，传统的人力管理方式逐渐无法满足需求，因此开发了这个系统。系统提供了分类管理信息的功能，并以旅游信息的具体方面作为模块划分依据，旨在提高信息管理效率，节省人力物力资源。

## 二·功能模块
系统包含以下主要功能模块：
1. **账号管理**：管理系统用户的账号信息。
2. **地区管理**：管理旅游地区的相关信息。
3. **景点信息管理**：管理旅游景点的信息。
4. **地方美食管理**：管理地方特色美食的信息。
5. **旅游线路管理**：管理旅游线路的信息。
6. **订单信息管理**：管理用户的旅游订单信息。
7. **新闻管理**：管理旅游相关的新闻信息。
8. **系统管理**：管理系统的设置和其他相关功能。

## 三·开发背景与意义
随着社会的发展和人们生活水平的提高，旅游成为放松压力和调节情绪的首选。计算机技术的普及使得人们习惯通过计算机获取旅游信息，并制定旅游方案。旅游信息管理系统应运而生，旨在节省人力物力，提高管理效率。

## 四·系统需求分析
系统需满足以下要求：
- 账号权限管理，分为管理员账号和游客账号。
- 展示旅游新闻。
- 提供留言功能。
- 管理账号、地区和景区信息。

## 五·系统设计思想
系统采用前后端分离技术，便于功能组合和修改。具备数据库维护功能，能够根据用户需求进行数据的添加、删除、修改、备份等操作。

## 六·系统开发步骤
1. 总体规划
2. 系统开发
   - 系统分析
   - 系统设计
   - 系统实施
3. 系统运行

## 七·技术介绍
- **B/S系统三层体系结构**：分为表示层（Web浏览器）、功能层（Web服务器）和数据层（数据库服务器）。
- **SpringBoot**：用于简化Spring应用的初始搭建及开发过程，提供快速便捷的开发体验。
- **Vue**：用于构建用户界面的渐进式框架，实现前后端分离的开发理念。

## 八·开发环境
- **服务器**：MacBookPro M1Pro
- **操作系统**：MacOS
- **客户端**：PC机,安装Web浏览器,即可使用
- **网络**：服务器和客户端应有网络连通，配置TCP/IP协议。

## 九·数据库设计
数据库设计的原则是减少数据冗余和重复，确保数据结构的稳定性。系统设计了多个数据库表，用于管理不同类型的信息，例如收藏记录、前端登录凭证、管理员、用户、新闻分类、新闻信息等。

## 十·系统实现
主要界面包括用户登录、首页、景点信息管理等。数据库连接通过配置文件读取数据库信息并实现连接。

## 十一·测试
系统测试包括单元测试、集成测试和系统测试，目的是在软件投入运行前尽可能多地发现错误，确保软件质量。

## 十二·总结
通过系统开发，提高了对系统分析、数据流图、数据字典等系统设计工具的认识，积累了宝贵的经验。

## 十三·致谢
感谢学校和指导老师在设计过程中的帮助和建议，使系统开发水平得到了提高。

## 十四·项目结构
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
