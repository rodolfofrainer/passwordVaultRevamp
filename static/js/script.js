$('#confirmDeleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var vaultItemId = button.data('vaultitemid');
    var form = $('#deleteForm');
    var actionUrl = form.attr('action').replace('0', vaultItemId);
    form.attr('action', actionUrl);
  });

function togglePasswordVisibility(itemId) {
    var passwordElement = document.getElementById("password" + itemId);
    var passwordValue = passwordElement.getAttribute("data-password");

    if (passwordElement.classList.contains('password-hidden')) {
      passwordElement.classList.remove('password-hidden');
      passwordElement.textContent = passwordValue;
    } else {
      passwordElement.classList.add('password-hidden');
      passwordElement.textContent = '******';
    }
  }