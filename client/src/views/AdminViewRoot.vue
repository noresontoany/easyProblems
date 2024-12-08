<script setup>
</script>

<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/students">
                Ученики
              </router-link>
            </button>
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/languages">
                Языки
              </router-link>
            </button>
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/lessons"> Темы </router-link>
            </button>
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/problems">
                Задачи
              </router-link>
            </button>
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/submissions">
                Отправки
              </router-link>
            </button>
            <button class="btn btn-outline-success me-3" type="button">
              <router-link class="nav-link" to="/study"> test </router-link>
            </button>

            <div class="btn-group">
              <button
                class="btn btn-secondary dropdown-toggle"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Dropdown
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="/admin">Admin</a></li>
                <li><a class="dropdown-item" href="#">Menu item</a></li>
                <li><a class="dropdown-item" href="#">Menu item</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script scoped>
</script>