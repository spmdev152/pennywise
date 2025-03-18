/**
 * Updates the user state after updating user details.
 * @param {CustomEvent} event - The hx-on::after-request event.
 */
function resetUserStateAfterUpdate(event) {
  const toast = document.getElementById("user-details-toast");

  if (toast.dataset.type === "success") {
    let data = document.getElementById("account-section");
    const newState = event.detail.requestConfig.parameters;

    data._x_dataStack[0]["firstName"] = newState["first_name"];
    data._x_dataStack[0]["username"] = newState["username"];
    data._x_dataStack[0]["originalFirstName"] = newState["first_name"];
    data._x_dataStack[0]["originalUsername"] = newState["username"];
  }
}
