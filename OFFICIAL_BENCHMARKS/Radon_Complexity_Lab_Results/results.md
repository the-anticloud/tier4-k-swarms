# Radon_Complexity_Lab_Results
**Project:** `K_SWARMS` | **Status:** `PASS` | **Run:** `2026-09-30T17:14:20.030944+00:00`

**Framework:** [Radon — Cyclomatic Complexity & Maintainability Index](https://radon.readthedocs.io/)

## Key Metrics

- **files_analyzed:** `10`
- **average_complexity:** `{'grade': 'A', 'score': 2.801418439716312}`
- **complexity_grade:** `A`
- **complexity_score:** `2.801418439716312`
- **mi_output:** `E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\example.py - A (100.00)
E:\fenta\Downloads\Th`

## Raw Output (first 50 lines)
```
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\scripts\examples.py
    F 4:0 get_example_py_urls - A (5)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\scripts\github_commits.py
    F 73:0 fetch_github_commits - D (24)
    F 43:0 parse_github_repo_url - B (6)
    F 24:0 _parse_date - A (5)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\scripts\llm_txt.py
    F 5:0 concat_all_md_files - B (9)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\swarms\env.py
    F 6:0 load_swarms_env - A (2)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\swarms\__init__.py
    F 18:0 __getattr__ - A (3)
    F 46:0 __dir__ - A (1)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SWARMS\UPSTREAM\tests\test_cli.py
    M 166:4 TestSetupArgumentParser.test_heavy_swarm_model_help_states_the_real_default - A (5)
    C 66:0 TestSetupArgumentParser - A (3)
    M 79:4 TestSetupArgumentParser.test_valid_commands_parse - A (3)
    C 570:0 TestCLIUtils - A (3)
    M 577:4 TestCLIUtils.test_colors_dict_has_required_keys - A (3)
    M 594:4 TestCLIUtils.test_detect_active_provider_no_keys - A (3)
    M 617:4 TestCLIUtils.test_detect_active_provider_multiple - A (3)
    M 75:4 TestSetupArgumentParser.test_returns_parser - A (2)
    M 105:4 TestSetupArgumentParser.test_default_yaml_file - A (2)
    M 110:4 TestSetupArgumentParser.test_custom_yaml_file - A (2)
    M 117
```

---
_Anticloud Independent Benchmark — 2026-09-30T17:14:20.030944+00:00_