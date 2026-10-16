import Lake
open Lake DSL

package «cosmology-genesis» where
  version := v!"0.1.0"

require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "v4.33.1"

lean_lib CosmologyGenesis
