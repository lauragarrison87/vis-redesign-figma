# Visualization Redesign 
To access the images directly in Figma, see [Figma Figure Design File](https://www.figma.com/file/J0bSgl1nLlq4aN601NRNex/Vis-Redesign?node-id=3%3A6291&t=owjBOEbjhjuW7JuA-1)

BEFORE creating your plot, determine: 
- **What message** is important to me to communicate, to **whom**, and **why**?
- What data do I want to show? Can I show it in one chart, or do I need to facet it out to help manage the visual complexity of the story that I want to tell?
    
For instance, in this example, I want to share a visual about the total computation needed to train popular AI vision systems according to academic/industry affiliation, ultimately to a lay audience. I want to show how industry may have lagged at first, but has since surpassed academic efforts in computational power. 

Below are some basic steps to consider for jazzing up your visualization into a detailed figure that communicates a message, using Figma. Note, these steps can also be applied directly in code as well, but it can take longer, and for me, I have found that I like the visual interface to quickly and easily prototype my visuals. 
1. Create your base plot in your tool of choice (I like to use vega-altair, but anything that will allow you to eventually save out a svg file works)
    - First attempt to show my data 
    - On the y-axis, I’m showing the total computation in petaFLOP, with no real information on what that means, which is a problem for my target audience. 
    - On the x-axis, I’m showing publication date by year of the system, and using color to map each system to its domain, shown in this legend at the top right. U
    - With my current visualization choice I'm not showing the attribute that I wanted to communicate (academic/industry affiliation), and the vision domain is hard to appreciate here. 
    ![Show the data](./redesign-figma/1-show-the-data.svg)
    - With faceting through small multiples, I can now show the academic affiliation of these different systems in a manageable way. The advantage of small multiples is that since each is essentially different versions of the same chart, once you can read one, you can read them all, making it easier to compare and find patterns (if that is a goal of the visualization)

    So now I’ve broken out the information I want to see, but it’s still hard to see what I’m getting at 

    ![Break up information, e.g., facet](./redesign-figma/2-break-up-info.svg)
2. Export your plot as svg
3. Create an empty Figma file 
4. Draw out a frame (hotkey: F) in the size of the Figure (e.g., half-width A4)
5. Drag your svg file into your Figma file window into the frame you just created, and adjust scale as needed
6. Based on message you want to communicate, if your data allow this, AND color is not part of the data encoding already, consider designing with grey. 
   - For instance, select all data points other than a given category of interest.
        - To directly select element of interest, hotkey: _cmd click_ on Mac, _ctrl shift 4_ on Windows; hold down _shift_ to select multiple objects, then group them to easily select later (hotkey: _cmd g_ on Mac, _ctrl g_ on Windows)
   - Then choose a grey value to assign to this group, and voila! You are managing to still show all of your data, but push it into the background so that it is no longer competing with your main story. 
   - Then, select your main category/data item, and choose a high-contrast color that will help make your data stand out. In my example, I have chosen orange.
   ![Design with grey](./redesign-figma/3-design-with-grey.svg)
7. Declutter your visualization to make it easier to read, e.g.,  
   - Reduce/remove gridlines
   - Remove unnecessary legends 
   - Don't make your viewer tilt their head to read your chart axis labels - no diagonal text, avoid vertical
   ![Declutter](./redesign-figma/4-declutter.svg)
8. Last, but not least: think about TEXT as just as important as the visuals in your figure! You want to tell your reader what they should learn from your figure, don't make them sit and try to puzzle it out themselves. This entails:
    - Move legends (if you still have after decluttering) closer to the actual data to improve readability
    - Write the title of your chart like a newspaper headline that captures the key takeaways of the chart and uses concise, active language
    - Add explainers that help clarify features in your visualization 
      - Captions/chart subtitle
      - Callout box - in my example, I have added a caption box that explains to my audience what a FLOP is
      - Add references to your data source
      - Add annotations (labels) on top of your chart to call out important features (for some types of data, this may be considered image manipulation and not be allowed, so if you ever are unsure, discuss with colleagues)
    ![Text + Vis = Joy](./redesign-figma/5-text+vis.svg)
9. Export your figure out from Figma:
   - Select your Figma frame
   - At the bottom of the right-hand panel, there is an Export menu. 
   ![Figma Export](./redesign-figma/export-menu.png)
   - For maximum resolution, export your figure as svg or pdf, if possible. If it must be a raster image file, use png. 
   
