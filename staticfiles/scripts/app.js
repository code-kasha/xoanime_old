document.addEventListener("DOMContentLoaded", () => {
  setupCache()
  handleCover()

  handleEpisodeSearch()
  handleTruncations()

  handleToggle("characters-button", "characters-container")
  handleToggle("openings-button", "openings-container")
  handleToggle("endings-button", "endings-container")
  handleToggle("relations-button", "relations-container")
  handleToggle("recommendations-button", "recommendations-container")

  handleSwitch("title-picker", "title-container")
  handleSwitch("desc-picker", "desc-container")

  scrollNowPlaying()

  function handleCover() {
    const cover = document.getElementById("cover")

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

  function handleEpisodeSearch() {
    const searchInput = document.getElementById("searchInput")
    const episodeLinks = Array.from(
      document.querySelectorAll("[data-type=episode]")
    )

    if (searchInput && episodeLinks) {
      const episodeNumbers = episodeLinks.map((link) =>
        link.innerText.toLowerCase()
      )

      searchInput.addEventListener("input", () => {
        const searchTerm = searchInput.value.toLowerCase()
        episodeLinks.forEach((link, index) => {
          const episodeNumber = episodeNumbers[index]
          link.classList.add("hidden")
          if (episodeNumber.includes(searchTerm)) {
            link.classList.remove("hidden")
          }
        })
      })
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

    if (item && container && provider == "mangadex") {
      container.innerText = item.value

      item.addEventListener("change", () => {
        container.innerText = item.value
      })
    }
  }

  function scrollNowPlaying() {
    window.addEventListener("DOMContentLoaded", (event) => {
      const currentEpisode = nowPlaying
      const episodeLink = document.getElementById(`episode-${currentEpisode}`)
      if (episodeLink) {
        episodeLink.scrollIntoView({
          behavior: "smooth",
          block: "center",
        })
      }
    })
  }

  function handleImageError() {
    if (imagePlaceholder) {
      this.src = imagePlaceholder
    }
  }

  function loadImageAndCache(imageId, imageSrc, imageUrl) {
    const img = new Image()
    img.setAttribute("data-type", "image")
    img.onload = () => {
      let item = localStorage.getItem(imageId)

      if (!item) {
        localStorage.setItem(imageId, imageSrc)
        if (navigator.serviceWorker.controller) {
          navigator.serviceWorker.controller.postMessage({
            action: "cache-image",
            imageId: imageId,
            imageSrc: imageSrc,
            imageUrl: imageUrl,
          })
        }
      }
    }

    img.onerror = function () {
      handleImageError.call(this)
    }
    img.src = imageSrc
  }

  function setupCache() {
    let cachedImageUrls = {}

    const images = document.querySelectorAll("[data-type=image]")
    if (images) {
      images.forEach((image) => {
        const imageId = image.alt
        const imageSrc = image.src
        const storedData = localStorage.getItem(imageId)

        if (storedData) {
          cachedImageUrls[imageId] = storedData
          cachedImageUrls[imageSrc] = imageSrc
        } else {
          cachedImageUrls[imageId] = ""
          cachedImageUrls[imageSrc] = ""
        }

        if (image.src && image.src !== imagePlaceholder) {
          image.onerror = handleImageError
        }
        loadImageAndCache(imageId, image.src, cachedImageUrls)
      })
    }
  }

  function setupSpinner() {
    const links = document.querySelectorAll("[data-action=fetch]")
    links.forEach((link) => {
      link.addEventListener("click", () => {
        document.getElementById("spinner-container").style.display = "flex"
      })
    })
  }
})
