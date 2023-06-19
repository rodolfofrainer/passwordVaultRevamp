$('#confirmDeleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var vaultItemId = button.data('vaultitemid');
    var form = $('#deleteForm');
    var actionUrl = form.attr('action').replace('0', vaultItemId);
    form.attr('action', actionUrl);
  });