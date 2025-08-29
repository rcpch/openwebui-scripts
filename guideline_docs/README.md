# Documents for RAG test

Scripts to download all the documents referenced from the RCPCH Guideline Directory: https://www.rcpch.ac.uk/resources/clinical-guideline-directory.

## List of links

To get all the links from this page I ran the following in Chrome Dev Tools on that page:

```javascript
anchors = [...document.querySelectorAll(".body-box li > a")]
text_and_link = anchors.map(a => [a.innerHTML, a.href])
console.log("text,link\n" + text_and_link.map(([text, link]) => `${text.replaceAll(",", "")},${link}`).join("\n"))
```

Needs the console.log otherwise it doesn't print newlines.

## Download all the files from the links

```
uv run analyse_links.py
domain
www.nice.org.uk         429
www.sign.ac.uk           17
www.rcpch.ac.uk          16
www.cclg.org.uk          11
www.rcophth.ac.uk         4
www.rcot.co.uk            3
www.bbuk.org.uk           3
www.rcog.org.uk           2
brit-thoracic.org.uk      2
ukkidney.org              2
www.headsmart.org.uk      2
www.chelwest.nhs.uk       2
www.resus.org.uk          1
www.bsaci.org             1
www.rcpsych.ac.uk         1
www.acb.org.uk            1
www.dsmig.org.uk          1
www.rcr.ac.uk             1
Name: count, dtype: int64
```

So probably only value in automating downloads for the NICE guidance.

Using this example: https://www.nice.org.uk/guidance/ng245/chapter/Rationale-and-impact. They very handily add a data tracking attribute
to their download guidance links. So we should be able to get the links by:

```javascript
document.querySelector("[data-track='guidancedownload']").href
'https://www.nice.org.uk/guidance/ng245/resources/asthma-diagnosis-monitoring-and-chronic-asthma-management-bts-nice-sign-pdf-66143958279109'
```