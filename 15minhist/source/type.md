Select Query Type
=========================

ServiceX supports multiple query backends to suit different workflows. Your choice depends on the data type and the complexity of your analysis.

| Uproot | FuncADL |
|--------|---------|
| ✅ Ideal for working with **ROOT ntuples** or flat data structures.<br>✅ Use preexisting knowledge of Uproot to build queries<br>✅ Queries run quickly and are easy to set up. | ✅ Designed for getting all possible data from **xAOD datasets**<br>✅ Allows writing queries in **Python syntax** that are translated into optimized C++ and run in AnalysisBase.<br>✅ Anything that can be done in AnalysisBase can be done with FuncADL.<br>✅ Removes need for cloning, changing, and building AnalysisBase. |
| ⚠️ Limited to simpler transformations and filtering.<br>⚠️ Does not natively handle complex object hierarchies. | ⚠️ Steeper learning curve; use only when necessary.<br>⚠️ Runs slower than Uproot ServiceX. |

For most analyses, Uproot queries will suffice. If you are not sure where to start, it is recommended to start there. 

If you frequently work with xAOD file types and need access to values beyond the standard set of objects, it is recommended that you start with FuncADL.

The rest of the tutorial will depend on the query type you choose. Please continue with the query type that best fits your analysis. Don’t worry as you can always go back later and try the other option if needed!
