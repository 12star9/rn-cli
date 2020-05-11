# React-Native基本项目模版 “脚手架”

项目工程变更为React-Native基本项目模版 “脚手架”!

🎉 背景: 之前主导开发一个React-Native项目和在编写自己的React-Native小应用的时候，发现很多开发步骤是必须经过的，为了今后下一个项目最大程度省去这些时间，把一些项目工程结构，调试配置，常用组件集成，原生端通信，原生组件封装等组装成一个开发模版“脚手架”！


#### 项目文件:

AwesomeProject:即react-native项目根文件夹,当前RN版本为0.59.0，对应React版本为16.8.3.
AwesomeProject子文件夹下的文件说明:
-  .vscode: VSCode IDE的调试配置文件.
-  .gitignore: 用来配置git提交需要忽略的文件.
-  package.json: package.json定义了项目所需要的各种模块，以及项目的配置信息;npm install命令根据这个配置文件，自动下载所需的模块，也就是配置项目所需的运行和开发环境。
-  __tests__: 测试文件夹，执行命令`npm test`会调用此文件夹下的测试文件进行执行，输出结果。
-  ios: ios的原生开发目录，可以用Xcode打开进行原生开发。
-  android: Android的原生开发目录，可以用Android Studio打开进行原生开发。
-  node_modules: 存放所有的项目依赖库，配置package.json之后执行“npm install”后自动创建的文件夹。
-  .buckconfig: buck的配置文件，buck是Facebook推出的一款高效率的App项目构建工具。
-  .flowconfig: Flow 是 Facebook 旗下一个为 JavaScript 进行静态类型检测的检测工具。它可以在 JavaScript 的项目中用来捕获常见的 bugs，比如隐式类型转换，空引用等等。
-  .gitattributes: git属性文件设定一些项目特殊的属性。比如要比较word文档的不同；对strings程序进行注册；合并冲突的时候不想合并某些文件等等。
-  .watchmanconfig: 用于监控bug文件和文件变化，并且可以出发指定的操作。
-  yarn.lock: Yarn 是 一个由 Facebook 创建的新 JavaScript 包管理器；每次添加依赖或者更新包版本，yarn都会把相关版本信息写入yarn.lock文件。这样可以解决同一个项目在不同机器上环境不一致的问题。
-  index.js: android 和 ios 入口文件，可以在android的MainApplication中的ReactNativeHost中重写getJSMainModuleName()方法更改; 在ios的AppDelegate.m文件的didFinishLaunchingWithOptions方法中通过jsBundleURLForBundleRoot可以更改入口文件。


#### 环境依赖
###### 1.按照React-Native官方[文档](https://facebook.github.io/react-native/docs/getting-started "文档")安装好对应的环境

###### 2.VSCode IDE依赖包安装
- 删除Console.*语句依赖: `yarn add --dev babel-plugin-transform-remove-console`
- VSCode智能提示: `npm install -g typings`，然后在项目根目录下`typings install dt~react-native --save --g`



#### 使用步骤
1. clone本项目到本地，安装项目重命名npm包: `yarn global add react-native-rename` or `npm install react-native-rename -g`，然后在项目根目录下打开终端输入命令: `react-native-rename "<new_project_name>" -b <bundle_id_name>`,ios端，打开Xcode,手动修改<bundle_id_name>
2. 修改AwesomeProject项目名为<new_project_name>
3. 执行`npm install`
4. 打包 `npm run bundle:ios` or `npm run bundle:android`,运行 `npm run ios:run` or 打开安卓模拟器，最后 `npm run android:run`

注意： 
如果出现问题，请核对对应的React(ReactNative)版本号，如果还是不行，麻烦提Issues！ 
建议还是按照官方文档来，该仓库下的代码还是有许多可以参考的！




#### 卸载RN第三方组件常用步骤:

##### react-native端:
1. package-lock.json删除组件对应配置代码.
2. 项目根目录打开终端执行: `npm install`.



##### 原生端:

###### 一.iOS

CocoaPods方式
1. 找到Podfile文件，删除组件对应pod配置代码.
2. os文件夹目录打开终端执行: `pod install`.

手动方式
1.  Library文件夹里删除组件对应库工程.
2. Build Phases里删除库和.bundle等资源引用.
3. Build Settings删除库引用路径(如果有).
4.  Info.plist删除库对应配置ID(如果有).
5. 原生工程代码里删除组件对应的引用代码.


###### 二.安卓
1. android文件夹目录下找到settings.gradle文件，删除库引用.
2. android/app文件夹目录下找到build.gradle文件，删除库依赖.
3. android/app/src/main/java/目录下找到MainApplication.java文件，删除组件的安卓原生代码引入.


#### 打包部署
package.json配置了常用的scripts，在react-native项目文件夹打开终端运行命令: `npm run <script-name>`
例如进行iOS打包: `npm run bundle:ios`


#### React-Native项目运行出错建议参考思路:
[StackOverFlow](https://stackoverflow.com/questions/tagged/react-native "StackOverFlow")
[React-Native-Issues](https://github.com/facebook/react-native/issues "React-Native-Issues")

我在出错的时候几乎全部从这两个地方找到解决思路的！








#### release各版本说明:

v0.0.1 集成GoogleMaps.








