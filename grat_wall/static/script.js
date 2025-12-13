const form = document.getElementById("grat-form")  // Create button
const input = document.getElementById("grat-input")  // text
const wall = document.getElementById("wall") // GET notes to display

// display wall
async function loadWall() {
    const res = await fetch("/grat");
    const grats = await res.json();
    render(grats);
}

loadWall();

// render notes on wall
function render(grats) {
    wall.innerHTML="";

    grats.forEach(text => {
        const li = document.createElement("li");
        li.textContent = text;
        wall.appendChild(li);
    });
}

// post notes to wall
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    if (!input.value.trim()) return;

    await fetch("/grat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: input.value })
    });

    input.value = "";
    loadWall();
})
