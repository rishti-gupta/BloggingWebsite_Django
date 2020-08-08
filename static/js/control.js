function openCreateForm() {
    closeForm();
    document.getElementById("myCreateForm").style.display = "block";

}
function openUpdateForm() {
    closeForm();
    document.getElementById("myUpdateForm").style.display = "block";
}
function openDeleteForm() {
    closeForm();
    document.getElementById("myDeleteForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myCreateForm").style.display = "none";
    document.getElementById("myDeleteForm").style.display = "none";
    document.getElementById("myUpdateForm").style.display = "none";
}