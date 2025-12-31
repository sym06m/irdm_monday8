def inject_tool_context(context, tool_output):
    return context + f"\nTool result: {tool_output}"


base_context = "Analyze business risk."
tool_output = "Market competition is high."

final_context = inject_tool_context(base_context, tool_output)
print(final_context)
