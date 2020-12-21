/**************************************
*   RayStarter
*
*   {{cookiecutter.project_name}}
*
*   This game has been created using raylib (www.raylib.com)
*   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
***************************************/
#include "{{cookiecutter.raylib_location}}"

// Include your stuff here!


// Main entry point
//-------------------------------------
int main(void)
{
    const int screenWidth = 640;
    const int screenHeight = 360;

    SetConfigFlags(FLAG_WINDOW_RESIZABLE | FLAG_VSYNC_HINT);
	
    InitWindow(screenWidth, screenHeight, "{{cookiecutter.project_name}}");
    SetWindowMinSize(screenWidth, screenHeight);

    while (!WindowShouldClose())
    {
        // Draw
        //-----------------------------
        BeginDrawing();
        ClearBackground(BLACK);
        DrawFPS(5,5);
        EndDrawing();
    }
	
    CloseWindow();
    return 0;
}