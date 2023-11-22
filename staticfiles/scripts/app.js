document.addEventListener("DOMContentLoaded", () => {
  handleCover()

  handleToggle("characters-button", "characters-container")
  handleToggle("openings-button", "openings-container")
  handleToggle("endings-button", "endings-container")
  handleToggle("relations-button", "relations-container")
  handleToggle("recommendations-button", "recommendations-container")

  handleSwitch("title-picker", "title-container")
  handleSwitch("desc-picker", "desc-container")

  handleTruncations()

  function handleCover() {
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

  function handleToggle(buttonId, containerId) {
    const button = document.getElementById(buttonId)
    const container = document.getElementById(containerId)

    if (button && container) {
      button.addEventListener("click", () => {
        container.classList.toggle("hidden")
      })
    }
  }

  function handleSwitch(itemId, containerId) {
    const item = document.getElementById(itemId)
    const container = document.getElementById(containerId)

    if (item && container) {
      container.innerText = item.value

      item.addEventListener("change", () => {
        container.innerText = item.value
      })
    }
  }
})
