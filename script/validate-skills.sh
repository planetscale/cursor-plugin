#!/usr/bin/env bash

set -euo pipefail

validate_skills_dir() {
  local root="$1"
  local label="$2"
  local summary_file="${GITHUB_STEP_SUMMARY:-}"
  local -a skill_files=()
  local -a skill_names=()

  if [[ ! -d "$root" ]]; then
    echo "::error::Missing skills directory: $root" >&2
    return 1
  fi

  mapfile -d '' -t skill_files < <(
    find "$root" -mindepth 2 -maxdepth 2 -type f -name 'SKILL.md' -print0 | sort -z
  )
  for skill_file in "${skill_files[@]}"; do
    skill_names+=("$(basename "$(dirname "$skill_file")")")
  done

  local count="${#skill_names[@]}"
  if (( count < 1 )); then
    echo "::error::No skills found in $root" >&2
    return 1
  fi

  local report="### $label ($count skills)\n"
  for skill_name in "${skill_names[@]}"; do
    report+="* \`$skill_name\`\n"
  done
  printf '%b' "$report"
  if [[ -n "$summary_file" ]]; then
    printf '%b' "$report" >> "$summary_file"
  fi
}

validate_skills_dir "database-skills/skills" "database-skills/skills"
validate_skills_dir "skills" "skills"
