const getCookie = (name) => {
  if (document.cookie && document.cookie !== "") {
    for (const cookie of document.cookie.split(";")) {
      const [key, value] = cookie.trim().split("=");
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
  }
};
const csrftoken = getCookie("csrftoken");

const toast = document.getElementById("js-toast");
let isVisivle = false;

const showToast = (status, message) => {
  if (isVisivle) return false;

  toast.innerHTML = message;
  toast.classList.add("is-" + status);
  toast.classList.add("is-show");
  isVisivle = true;
};

toast.addEventListener("animationend", () => {
  toast.innerHTML = "";
  toast.className = "toast";
  isVisivle = false;
});
