public class ConfigManager {

    private String config;
    private String data;

    public ConfigManager(String config, String data) {
        this.config = config;
        this.data = data;
    }

    public void printConfig() {
        System.out.println("Config: " + config);
    }

    public void printData() {
        System.out.println("Data: " + data);
    }

    public static void main(String[] args) {
        ConfigManager manager = new ConfigManager("v1.0", "User settings");
        manager.printConfig();
        manager.printData();
    }
}
