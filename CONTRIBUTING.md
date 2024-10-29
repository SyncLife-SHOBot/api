# Estrategia de Ramificación y Convenciones de Commits

Este documento describe la estrategia de ramificación, el flujo de trabajo y
las convenciones de commits que seguimos en este repositorio.

## Estructura de Ramas

- `main`: Rama principal que contiene el código en producción
- `develop`: Rama de desarrollo donde se integran todas las nuevas características
- `feature/*`: Ramas temporales donde se desarrollan nuevas características

## Convenciones de Commits

Seguimos la especificación de
[Conventional Commits](https://www.conventionalcommits.org/) para todos
nuestros commits y títulos de Pull Requests.

### Estructura del Commit

```txt
<tipo>[alcance opcional]: <descripción>

[cuerpo opcional]

[nota de pie opcional]
```

### Tipos de Commits

- `feat`: Nuevas características
- `fix`: Correcciones de errores
- `docs`: Cambios en documentación
- `style`: Cambios que no afectan el significado del código (espacios,
formateo, etc.)
- `refactor`: Cambios de código que no corrigen errores ni añaden funcionalidad
- `test`: Añadir o corregir tests
- `chore`: Cambios en el proceso de build o herramientas auxiliares

### Ejemplos

```txt
feat(auth): añadir autenticación con Google
fix(api): corregir error en endpoint de usuarios
docs(readme): actualizar instrucciones de instalación
style: ajustar indentación en archivos CSS
```

### Convenciones para Pull Requests

- El título del PR debe seguir el mismo formato de Conventional Commits
- Ejemplo: `feat(user-profile): añadir página de perfil de usuario`

## Flujo de Trabajo

### Desarrollo de Nuevas Características

1. Los desarrolladores deben crear una nueva rama desde `develop` para cada
nueva característica:

   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nombre-caracteristica
   ```

2. Realizar commits en la rama feature mientras se desarrolla la
característica, siguiendo las convenciones de commits.

3. Cuando la característica está lista, crear un Pull Request (PR) hacia `develop`.

4. Una vez que el PR es aprobado y fusionado, la rama `feature/*` debe ser eliminada.

### Actualizaciones a Producción

1. Las fusiones a la rama `main` están restringidas y solo pueden ser
realizadas por el dueño del repositorio.

2. Periódicamente, el código en `develop` se fusiona en `main`:

   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```

## Reglas Importantes

- ✅ Toda nueva característica debe partir desde `develop`
- ✅ Los PRs siempre deben dirigirse a `develop`
- ✅ Las ramas de feature deben eliminarse después de ser fusionadas
- ✅ Todos los commits deben seguir la convención Conventional Commits
- ❌ No hacer commits directamente en `main`
- ❌ No hacer commits directamente en `develop`
- ❌ No usar mensajes de commit genéricos o poco descriptivos

## Diagrama de Flujo

```txt
main    ────────────●─────────────────●──────
                    ↑                 ↑
develop  ────●────●─●─────●────●──────●──────
              ↑     ↑     ↑    ↑
feature-1     ●─────●     
                          ●────●
feature-2                      ↑
```

## Comandos Útiles

```bash
# Crear nueva rama feature
git checkout -b feature/nueva-caracteristica develop

# Actualizar rama develop local
git checkout develop
git pull origin develop

# Eliminar rama feature local y remota después de fusionar
git branch -d feature/nombre-caracteristica
git push origin --delete feature/nombre-caracteristica

# Ejemplo de commit siguiendo convenciones
git commit -m "feat(login): añadir validación de contraseña"
```
