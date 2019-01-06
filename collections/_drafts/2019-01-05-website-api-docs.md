---
title: HTML, SASS/CSS, and JS API Documentation
categories: [projects, homepage]
tags: [js, html, css, sass]
---
Documentation for the webpage as of `"{% include ref-commit.html text="" commit="" %}"`.

## HTML

#### General Layout
```html
<!doctype html>
<html lang="en">
    <head />
    <body>
        <div class="container-fill">
            <div class="row" id="header-row">
                <a id="logo" />
                <nav id="main-nav" />
            </div>
            <div class="row" id="main-row"><!-- Main section -->
                <div class="col" id="left-col" /><!-- Left side content -->
                <div class="col-8 main blog-page in-main" id="main-col" /><!-- Content -->
                <div class="col" id="right-col" /><!-- Right side content -->
            </div>
            <div class="row" id="footer-row" />
        </div>
    </body>
</html>
```

#### Classes
All classes are defined by Bootstrap except for the following:

 Class Name | Location | Description
 --- | --- | ---
main | .container-fill > div[2] > div[2] |  Element which contains main content.
`{page.title}`-page | .main | Element which contains content of `page`
in-`{page.collection}`  | .main  |  Element which contains content of a page in `page.collection`

#### ID's
 ID Name | Description
 --- | ---
 logo | Element that should be placed in the top left corner of the site
main-nav  |  Nav menu for the whole site
header-row  |  Header
main-row  |  Bootstrap row for the main content
left-col  |  Left column in main content
main-col  |  Main column, where `page.content` is inserted
right-col |  Right column in main content
footer-row  |  Footer

## SASS/CSS
Information is separated into different areas. Selectors are excluded from
the `__init__` folder, and global variable declaration is excluded from the `base` and `pages` folders (except for `base/theme.scss`).

All folders have an `_init.scss` file which imports all of the files in its directory in the correct order.
```
_sass/
├── base.scss             - base.scss imports everything
├── __init__/             - __init__/ holds the initialization stuff, i.e.
│   ├── mixins/...          the global mixins, color settings, and theme for the site.
│   ├── theme.scss
│   └── vars              - Holds values for use in the site. Should be referenced by
│       ├── colors.scss     __init__/theme.scss, and by nobody else.
│       └── fonts.scss
├── base/                 - Holds base config settings. config.scss only selects by tag,
│   ├── config.scss         and site.scss selects by class and id, setting the arrangement
│   ├── site.scss           of the site. syntax.scss handles class selectors for syntax
│   └── syntax.scss         highlighting of pre > code blocks.
└── pages/                - Page specific css stuff.
    ├── home.scss
    ├── post.scss
    └── resources.scss
```

#### Initialization variables
Holds mixins in `mixins.scss`, most notably `dynamic-extend`, and the site theme in `theme.scss`. Variables should
first be declared in `theme.scss` before being used elsewhere.

## JavaScript API
