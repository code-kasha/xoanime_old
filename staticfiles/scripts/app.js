document.addEventListener("DOMContentLoaded", () => {
  handleTruncations()
  checkCover()

  function handleTruncations() {
    items = document.getElementsByClassName("truncate")
    if (items) {
      Array.from(items).forEach((item) =>
        item.addEventListener("click", () => {
          item.classList.toggle("truncate")
        })
      )
    }
  }

  function checkCover() {
    const cover = document.querySelector("[data-type='cover']")

    if (cover) {
      const img = new Image()

      img.onload = function () {
        const width = this.naturalWidth
        const height = this.naturalHeight

        if (width > height) {
          cover.classList.remove("hidden")
        }
      }

      img.src = cover.src
    }
  }
})
