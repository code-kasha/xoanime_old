document.addEventListener("DOMContentLoaded", () => {
  let currentPageIndex = 1
  let isSinglePageMode = 1

  setupKeys()
  setupNavButtons()
  setupToggle()

  function setupKeys() {
    document.addEventListener("keyup", function (e) {
      if (isSinglePageMode) {
        switch (e.key) {
          case "ArrowRight":
            nextPage()
            break

          case "ArrowLeft":
            previousPage()
            break

          case "t":
            toggleMode()
            break
        }
      }
    })
  }

  function setupToggle() {
    const toggler = document.getElementById("mode-switcher")

    toggler.addEventListener("click", () => {
      toggleMode()
    })
  }

  function setupNavButtons() {
    const next = document.getElementById("next-page")
    const previous = document.getElementById("previous-page")

    if (next) {
      next.addEventListener("click", function () {
        nextPage()
      })
    }

    if (previous) {
      previous.addEventListener("click", function () {
        previousPage()
      })
    }
  }

  function showPage(pageNumber) {
    const pages = document.querySelectorAll(".page")
    pages.forEach((page) => {
      page.classList.add("hidden")
    })

    const currentPage = document.querySelector(`.page:nth-child(${pageNumber})`)
    currentPage.classList.remove("hidden")
  }

  function previousPage() {
    if (currentPageIndex > 1) {
      currentPageIndex--
      showPage(currentPageIndex)
    }
  }

  function nextPage() {
    const totalPages = document.querySelectorAll(".page").length
    if (currentPageIndex < totalPages) {
      currentPageIndex++
      showPage(currentPageIndex)
    }
  }

  function toggleMode() {
    const pages = document.querySelectorAll(".page")
    const buttons = document.querySelectorAll("[data-type=single]")
    const list = document.getElementById("chapter-list")

    if (isSinglePageMode) {
      pages.forEach((page) => {
        page.classList.remove("hidden")
      })
    } else {
      showPage(currentPageIndex)
    }

    buttons.forEach((button) => {
      button.classList.toggle("hidden")
    })
    list.classList.toggle("hidden")
    list.classList.toggle("grid")

    isSinglePageMode = !isSinglePageMode
  }
})
